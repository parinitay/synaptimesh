import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.command_router import route_command

from backend.command_router import route_command

print(route_command("open_chatgpt", 0.90))
print(route_command("open_gmail", 0.90))
print(route_command("compose_email", 0.90))
print(route_command("search_python_tutorial", 0.90))
print(route_command("open_notepad", 0.90))