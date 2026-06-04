
import webbrowser


def execute_browser_command(command):

    if command == "open_google":
        webbrowser.open("https://www.google.com")

    elif command == "open_youtube":
        webbrowser.open("https://www.youtube.com")

    elif command == "open_gmail":
        webbrowser.open("https://mail.google.com")

    elif command == "open_chatgpt":
        webbrowser.open("https://chatgpt.com")

    elif command == "compose_email":
        webbrowser.open(
            "https://mail.google.com/mail/u/0/#inbox?compose=new"
        )

    elif command == "search_python_tutorial":
        webbrowser.open(
            "https://www.youtube.com/results?search_query=python+tutorial"
        )

    elif command == "search_java_tutorial":
        webbrowser.open(
            "https://www.youtube.com/results?search_query=java+tutorial"
        )

    elif command == "search_mqtt_tutorial":
        webbrowser.open(
            "https://www.youtube.com/results?search_query=mqtt+tutorial"
        )

    else:
        print(f"Unknown browser command: {command}")