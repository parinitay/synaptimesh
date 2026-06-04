from backend.command_registry import VALID_COMMANDS
from backend.browser_automation import execute_browser_command
from backend.media_automation import execute_media_command
from backend.mouse_automation import execute_mouse_command
from backend.application_automation import execute_application_command


def dispatch(command):

    category = VALID_COMMANDS.get(command)

    if category == "browser":
        execute_browser_command(command)

    elif category == "media":
        execute_media_command(command)

    elif category == "mouse":
        execute_mouse_command(command)

    elif category == "application":
        execute_application_command(command)

    else:
        print(f"Unknown command: {command}")