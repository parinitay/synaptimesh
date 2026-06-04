import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from backend.command_router import route_command

print("===== Mouse Automation Test =====")

print(route_command("hover_center", 0.90))

input("Press Enter...")

print(route_command("move_left", 0.90))

input("Press Enter...")

print(route_command("move_right", 0.90))

input("Press Enter...")

print(route_command("move_up", 0.90))

input("Press Enter...")

print(route_command("move_down", 0.90))

input("Press Enter...")

print(route_command("scroll_down", 0.90))

input("Press Enter...")

print(route_command("scroll_up", 0.90))

input("Press Enter...")

print(route_command("left_click", 0.90))

input("Press Enter...")

print(route_command("right_click", 0.90))

input("Press Enter...")

print(route_command("double_click", 0.90))