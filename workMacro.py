
import pyautogui
import keyboard


def Disposition():
    print("Select a Disposition for the call: \nAns. Mach. = '-'\nNo Answer = '*'\nDisconnected = '/'\n")
    keyboard.read_event()
    if keyboard.is_pressed('-'):
        # Dispositions as Answering Machine
        print("Answering Machine")
        pyautogui.moveTo(669, 331)
        pyautogui.click()
    elif keyboard.is_pressed('*'):
        # Dispositions as No Answer
        print("No Answer")
        pyautogui.moveTo(1026, 384)
        pyautogui.click()
    elif keyboard.is_pressed('/'):
        # Dispositions as Disconnected
        print("Disconnected")
        pyautogui.moveTo(722, 502)
        pyautogui.click()


def HangUp():
    print("Hanging Up...")
    pyautogui.moveTo(177, 565)
    pyautogui.click()

    Disposition()


def DialNext():
    print("Dialing Next...")
    pyautogui.moveTo(188, 225)
    pyautogui.click()
    keyboard.wait('-')
    HangUp()


def main():
    loopTracker = True

    print("Spooling Up...")

    while loopTracker:

        print("\nPress + to Dial\nPress * to quit\n")
        keyboard.read_event()
        if keyboard.is_pressed('+'):
            DialNext()
        elif keyboard.is_pressed('*'):
            loopTracker = False


if __name__ == "__main__":
    main()
