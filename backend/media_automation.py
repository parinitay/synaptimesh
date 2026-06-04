import webbrowser
import pyautogui
import time


def execute_media_command(command):

    if command == "open_song":

        # Opens YouTube song
        webbrowser.open(
            "https://www.youtube.com/watch?v=JGwWNGJdvx8"
        )

        print("Opening YouTube Song...")

        time.sleep(5)

        # Press K to play video
        pyautogui.press("k")

        print("Playing Song")

    elif command == "pause_song":

        pyautogui.press("k")

        print("Song Paused")

    elif command == "resume_song":

        pyautogui.press("k")

        print("Song Resumed")

    elif command == "volume_up":

        for _ in range(5):
            pyautogui.press("volumeup")

        print("Volume Increased")

    elif command == "volume_down":

        for _ in range(5):
            pyautogui.press("volumedown")

        print("Volume Decreased")

    else:

        print(f"Unknown media command: {command}")