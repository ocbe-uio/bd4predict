from fastapi import FastAPI
from app.backend import (
    make_prediction,
    pd,
    TimingMiddleware,
    load_model,
    MapieConformalPredictiveDistribution
)
from app.schemas import PredictionRequest, PredictionResponse
from typing import Dict


MapieConformalPredictiveDistribution = MapieConformalPredictiveDistribution

model = load_model(model_path = "models/reduced_conformal_lasso_ghs.pkl")

description = " \n" "## Endpoints: \n" "- **/predict/** \n"

app = FastAPI(
    title="BD4Predict API",
    description=description,
    summary="This API is a wrapper for the BD4Predict backend.",
    version="1.0.0",
    terms_of_service="Check the MIT license.",
    contact={
        "name": "Mauricio Moreira Soares",
        "url": "http://phydev.github.io",
        "email": "phydev@protonmail.ch",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/license/mit",
    },
    #lifespan = lifespan
)

app.add_middleware(TimingMiddleware)

@app.get("/")
async def root():
    return {
        "message": (
            "BD4Predict API is up and running!"
            " For documentation access /docs"
            " (Swagger UI) or /redoc (ReDoc)"
        )
    }


# make prediction
@app.post("/predict/", response_model=PredictionResponse)
async def predict(patient_data: PredictionRequest) -> Dict:
    """
    This endpoint returns a prediction based on the input data.
    """
    
    patient_data = pd.DataFrame(patient_data.dict(), index=[0])

    response = make_prediction(patient_data, model)

    return response


if __name__ == "__main__":
    # run rest api with uvicorn
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
