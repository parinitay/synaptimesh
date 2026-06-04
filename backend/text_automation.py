import pyautogui
import time

def execute_text_command(command):

    if command == "write_hello":
        time.sleep(2)
        pyautogui.write("Hello from EEG System!")