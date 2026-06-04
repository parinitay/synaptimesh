import os


def execute_application_command(command):

    if command == "open_notepad":
        os.system("start notepad")

    elif command == "open_calculator":
        os.system("start calc")