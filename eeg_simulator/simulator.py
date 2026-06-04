import requests
import random
import time

commands = [
    "LEFT",
    "RIGHT",
    "UP",
    "DOWN",
    "SELECT"
]

while True:

    payload = {
        "command": random.choice(commands),
        "confidence": round(
            random.uniform(0.7,1.0),
            2
        )
    }

    requests.post(
        "http://localhost:8000/command",
        json=payload
    )

    print(payload)

    time.sleep(2)