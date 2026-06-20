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
        key=lambda x: abs(x-distance)
    )

    return battery_curve[closest_distance]



def predict_soc(
        current_soc,
        distance,
        traffic
):

    factor = get_condition_factor(traffic)


    # converts real distance into
    # effective battery distance

    effective_distance = (
        distance * factor
    )


    predicted_soc = get_soc_from_curve(
        effective_distance
    )


    # adjust according to starting SOC

    soc_difference = (
        100 - predicted_soc
    )


    final_soc = (
        current_soc - soc_difference
    )


    if final_soc < 20:

        return {
            "predicted_soc": round(final_soc,2),
            "charging_required": True,
            "message":
            "Battery level unsafe. Charging recommended."
        }


    else:

        return {
            "predicted_soc": round(final_soc,2),
            "charging_required": False,
            "message":
            "Destination reachable safely."
        }
