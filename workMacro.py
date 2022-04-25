import pyautogui
import keyboard


def DialNext():
    print("Dialing Next...")
    pyautogui.moveTo(188, 225, duration=1)
    pyautogui.click()


def HangUp():
    print("Hanging Up...")
    pyautogui.moveTo(177, 565, duration=1)
    pyautogui.click()


print("Spooling Up...")
while keyboard.read_key() != "*":
    if keyboard.read_key() == "1":
        DialNext()
    elif keyboard.read_key() == "2":
        HangUp()
    elif keyboard.read_key() == "*":
        print("Quitting Process")
