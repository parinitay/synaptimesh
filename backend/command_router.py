from mqtt_client import publish_command

latest_command = {
    "command": "NONE",
    "confidence": 0
}

def route_command(command, confidence):

    latest_command["command"] = command
    latest_command["confidence"] = confidence

    publish_command(command)

    return {
        "status": "success"
    }