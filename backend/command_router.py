from backend.mqtt_client import publish_command
from backend.dispatcher import dispatch
from backend.command_registry import VALID_COMMANDS

CONFIDENCE_THRESHOLD = 0.75

latest_command = {
    "command": "NONE",
    "confidence": 0
}


def route_command(command, confidence):

    # Confidence Validation
    if confidence < CONFIDENCE_THRESHOLD:
        return {
            "status": "rejected",
            "reason": "low confidence",
            "command": command,
            "confidence": confidence
        }

    # Command Validation
    if command not in VALID_COMMANDS:
        return {
            "status": "rejected",
            "reason": "invalid command",
            "command": command,
            "confidence": confidence
        }

    # Store Latest Command
    latest_command["command"] = command
    latest_command["confidence"] = confidence

    # Execute Command
    dispatch(command)

    # Publish via MQTT
    publish_command(command)

    return {
        "status": "success",
        "command": command,
        "confidence": confidence
    }


def get_latest_command():
    return latest_command
    