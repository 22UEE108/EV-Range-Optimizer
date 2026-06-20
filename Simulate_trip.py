import requests
import time


updates = [
    {
        "current_soc":70,
        "remaining_distance":100,
        "traffic":"medium"
    },

    {
        "current_soc":60,
        "remaining_distance":80,
        "traffic":"high"
    },

    {
        "current_soc":45,
        "remaining_distance":50,
        "traffic":"high"
    }
]


for data in updates:

    response = requests.post(
        "http://127.0.0.1:8000/update-trip",
        json=data
    )

    print(response.json())

    time.sleep(5)
