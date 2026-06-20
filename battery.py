import json


with open("battery_profile.json") as file:
    battery_curve = json.load(file)


battery_curve = {
    int(distance): soc
    for distance, soc in battery_curve.items()
}



def get_condition_factor(traffic):

    factors = {
        "low": 1.0,
        "medium": 1.2,
        "high": 1.4
    }

    return factors.get(
        traffic.lower(),
        1.0
    )



def get_soc_from_curve(distance):

    closest_distance = min(
        battery_curve.keys(),
        key=lambda x: abs(x - distance)
    )

    return battery_curve[closest_distance]



def calculate_prediction(
        current_soc,
        distance,
        traffic
):

    factor = get_condition_factor(traffic)


    # adjusted distance based on conditions
    effective_distance = (
        distance * factor
    )


    expected_soc = get_soc_from_curve(
        effective_distance
    )


    # energy consumed from 100% reference
    energy_used = (
        100 - expected_soc
    )


    predicted_soc = (
        current_soc - energy_used
    )


    if predicted_soc < 20:

        return {
            "predicted_soc": round(predicted_soc,2),
            "charging_required": True,
            "message":
            "Battery unsafe. Find charging station."
        }


    return {
        "predicted_soc": round(predicted_soc,2),
        "charging_required": False,
        "message":
        "Trip conditions acceptable."
    }
        
