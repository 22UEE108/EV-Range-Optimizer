from fastapi import FastAPI

from models import (
    TripInput,
    PredictionResult
)

from battery import predict_soc



app = FastAPI(
    title="EV Range Optimizer"
)



@app.get("/")
def home():

    return {
        "status":
        "EV Range Optimizer Running"
    }



@app.post(
    "/predict",
    response_model=PredictionResult
)
def predict(
    trip: TripInput
):

    result = predict_soc(
        trip.soc,
        trip.distance,
        trip.traffic
    )


    return result
