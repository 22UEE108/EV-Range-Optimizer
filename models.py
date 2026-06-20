from pydantic import BaseModel



class TripInput(BaseModel):

    soc: float
    distance: float
    traffic: str



class UpdateTrip(BaseModel):

    current_soc: float
    remaining_distance: float
    traffic: str



class PredictionResult(BaseModel):

    predicted_soc: float
    charging_required: bool
    message: str
