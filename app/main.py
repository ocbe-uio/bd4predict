from fastapi import FastAPI
from app.backend import (
    make_prediction,
    pd,
    TimingMiddleware,
    load_model,
    MapieConformalPredictiveDistribution
)
from app.schemas import PredictionRequest, PredictionResponse
from fastapi.middleware.cors import CORSMiddleware
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

# recommended
# allow_origins=["https://yourdashboarddomain.com", "http://localhost:3000"],  # Example


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust this in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, consider narrowing this down to what you use
    allow_headers=["*"],  # Allows all headers, consider narrowing this down as well
    )

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
    
    patient_data = pd.DataFrame(patient_data.model_dump(), index=[0])

    response = make_prediction(patient_data, model)

    return response


if __name__ == "__main__":
    # run rest api with uvicorn
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")
