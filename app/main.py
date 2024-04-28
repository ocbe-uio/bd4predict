from fastapi import FastAPI
from app.backend import (
    is_valid_id_number,
    get_age_from,
    get_gender_from,
    run_awk,
    stratified_valid_numbers,
    TimingMiddleware,
)
from pydantic import BaseModel, Field
from app.backend import *
from typing import Dict

description = (
    " \n"
    "## Endpoints: \n"
    "- **/predict/** \n"

)


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
)

app.add_middleware(TimingMiddleware)


# Pydantic model definitions for the responses
class PredictionResponse(BaseModel):
    valid: bool = True
    gender: str = "female"
    age: int = 32
    lines: list = ["4", "5"]
    total_valid_id_numbers: int = 34506
    range_0_19: int = Field(..., alias="0-19")
    range_20_64: int = Field(..., alias="20-64")
    range_above_65: int = Field(..., alias=">=65")
    male: AgeGroups
    female: AgeGroups


@app.get("/")
async def root():
    return {
        "message": (
            "Sigma API is up and running!"
            " For documentation access /docs"
            " (Swagger UI) or /redoc (ReDoc)"
        )
    }


# check if an id number is valid
@app.post("/validate", response_model = PredictionResponse)
async def predict(patient_data) -> Dict:
    """
    This endpoint returns a prediction based on the input data.
    """
    
    model = 'models/reduced_conformal_lasso_ghs.pkl'

    response = {"prediction": predict(patient_data, model)}

    return response
    




if __name__ == "__main__":
    # run rest api with uvicorn
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8070, log_level="info")
