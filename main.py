from fastapi import FastAPI


from models import (
    TripInput,
    UpdateTrip,
    PredictionResult
)


from battery import calculate_prediction



app = FastAPI(
    title="EV Range Optimizer"
)



@app.get("/")
def home():

    return {
        "message":
        "EV Range Optimizer Running"
    }




# Before journey

@app.post(
    "/predict",
    response_model=PredictionResult
)
def predict(
    trip: TripInput
):

    result = calculate_prediction(
        trip.soc,
        trip.distance,
        trip.traffic
    )

    return result




# During journey updates

@app.post(
    "/update-trip",
    response_model=PredictionResult
)
def update_trip(
    update: UpdateTrip
):

    result = calculate_prediction(
        update.current_soc,
        update.remaining_distance,
        update.traffic
    )


    return result

