import pyautogui


def execute_mouse_command(command):

    if command == "scroll_down":

        pyautogui.scroll(-500)

    elif command == "scroll_up":

        pyautogui.scroll(500)

    elif command == "left_click":

        pyautogui.click()

    elif command == "right_click":

        pyautogui.rightClick()

    elif command == "double_click":

        pyautogui.doubleClick()

    elif command == "move_left":

        pyautogui.moveRel(-200, 0, duration=0.5)

    elif command == "move_right":

        pyautogui.moveRel(200, 0, duration=0.5)

    elif command == "move_up":

        pyautogui.moveRel(0, -200, duration=0.5)

    elif command == "move_down":

        pyautogui.moveRel(0, 200, duration=0.5)

    elif command == "hover_center":

        screen_width, screen_height = pyautogui.size()

        pyautogui.moveTo(
            screen_width // 2,
            screen_height // 2,
            duration=1
        )

    else:

        print(f"Unknown mouse command: {command}")