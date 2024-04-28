"""
This file contains helper functions used in the API.
"""

from typing import Type, Dict, Union
import pandas as pd
import numpy as np
import pickle

# for custom logging
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint)
from starlette.requests import Request
from starlette.responses import Response
import time
import logging


def imputation(data: pd.DataFrame, 
               model) -> pd.DataFrame:
    '''
    impute the missing values in the data using the model pipeline
    and back-transform the data to retrieve them in the original scale

    Nomenclature:
    _in: original features
    _out: features after transformation

    '''
    
    num_features = model.named_steps['preprocessing'].named_transformers_['num'].get_feature_names_out()
    cat_features_in = model.named_steps['preprocessing'].named_transformers_['cat'].feature_names_in_
    cat_features_out = model.named_steps['preprocessing'].named_transformers_['cat'].get_feature_names_out()

    processed_data = model.named_steps['preprocessing'].transform(data)

    features_out = num_features.tolist() + cat_features_out.tolist()

    processed_data = pd.DataFrame(processed_data, columns = features_out)

    num_imputed = model.named_steps['preprocessing'].named_transformers_['num'].named_steps['scale'].inverse_transform(processed_data[num_features])
    cat_imputed = model.named_steps['preprocessing'].named_transformers_['cat'].named_steps['onehot'].inverse_transform(processed_data[cat_features_out])
    imputed = np.concatenate((num_imputed, cat_imputed), axis=1)

    features_in = num_features.tolist() + cat_features_in.tolist()

    imputed = pd.DataFrame(imputed, columns = features_in, index = data.index)

    return imputed



from mapie.regression import MapieRegressor


class MapieConformalPredictiveDistribution(MapieRegressor):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.conformity_score.sym = False

    def get_cumulative_distribution_function(self, X, y_pred):
        '''
        this is based on the paper: 
        "Nonparametric predictive distributions based on conformal prediction" (2017) 
        Vovk et al 

        get_estimation_distribution() computes the Equation (22) in the paper
            C_i = \hat{y}_{n+1} + (y_i + \hat{y}_i) 
            np.add(y_hat, conformity_scores)
        then it can be sorted in increasing order to obtain the predictive distribution
        '''
        
        cs = self.conformity_scores_[~np.isnan(self.conformity_scores_)]

        res = self.conformity_score_function_.get_estimation_distribution(
            X, y_pred.reshape((-1, 1)), cs
        )
        return res

    def find_nearest(self, array, value):
        '''
        find the closest value in array
        '''
        array = np.asarray(array)
        value = np.asarray(value)
        idx = (np.abs(array - value.reshape(-1,1))).argmin(axis=1)
        return idx[0]


    def predict_proba(self, X, lower = None, upper = None):
        y_pred = self.predict(X)
        y_cdf = self.get_cumulative_distribution_function(X, y_pred)
        probability = np.zeros((X.shape[0]))
        
        for observation in range(X.shape[0]):
            counts, bins = np.histogram(y_cdf[observation], bins=100)
            cdf = np.cumsum(counts)/np.sum(counts)
        
            if lower is not None:
                #indices = self.find_nearest(bins, lower).reshape(-1,1)
    
                probability[observation] =  cdf[self.find_nearest(bins, lower)-1] #np.take_along_axis(cdf, indices = indices, axis = 1)
                #probability =  cdf[ self.find_nearest(bins, upper) ] - cdf[ self.find_nearest(bins, lower) ]
            else:
                probability = cdf[ self.find_nearest(bins, y_pred) -1 ]
            
        return probability

def make_integer(x):
    try:
        return int(x)
    except ValueError:
        return x
    

def get_explainability(patient_data, model):
    """
    // to be implemented

    This function returns single explanability with
    shapley values for the prediction based on the input data.
    :param patient_data: the input data
    :param model: the model to use for prediction
    :return: the explanation
    """
    
    explanation = None

    return explanation

def make_prediction(patient_data: pd.DataFrame, model) -> Dict:
    """
    This function returns the prediction based on the input data.
    :param patient_data: the input data
    :param model: the model to use for prediction
    :return: the prediction
    """
    df = pd.DataFrame(data = patient_data, index = [0])

    # Replace negative values with np.nan
    
    df = df.apply(lambda x: x.where(x >= 0, np.nan) 
                    if np.issubdtype(x.dtype, np.number) 
                    else x
                    )


    # load the model
    with open(model, 'rb') as file:
        model = pickle.load(file)

    imputed_data = imputation(df, model)

    result = model.predict(df)

    decline_probability = model.predict_proba(df, lower = imputed_data['hn3_dv_c30_ghs'] - 10)
    
    y_cdf = model.named_steps['regressor'].get_cumulative_distribution_function(df, result)

    ci = np.quantile(y_cdf, [0.025, 0.975])

    prediction = {
        'predicted_value': result[0],
        'ci': ci.tolist(),
        'decline_probability': decline_probability[0],
        'conformal_predictive_distribution': y_cdf[0].tolist(),
        'imputation': imputed_data.map(make_integer).to_dict(orient='records')[0]
        }

    return prediction




class TimingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.logger = logging.getLogger("uvicorn.error")

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        self.logger.info(
            f"{request.method} {request.url} - \
                {response.status_code}: \
                    Response time: {process_time:.5f}s"
        )
        return response