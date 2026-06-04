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

print("===== Media Automation Test =====")

print(route_command("open_song", 0.90))

input("Song Opened. Press Enter to Pause...")

print(route_command("pause_song", 0.90))

input("Press Enter to Resume...")

print(route_command("resume_song", 0.90))

input("Press Enter for Volume Up...")

print(route_command("volume_up", 0.90))

input("Press Enter for Volume Down...")

print(route_command("volume_down", 0.90))