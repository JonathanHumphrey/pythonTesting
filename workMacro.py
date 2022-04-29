
import pyautogui
import keyboard


def Disposition():
    print("Select a Disposition for the call: \nAns. Mach. = '-'\nNo Answer = '*'\nDisconnected = '/'\n")
    keyboard.read_key()
    if keyboard.read_key() == '-':
        # Dispositions as Answering Machine
        print("Answering Machine")
        pyautogui.moveTo(669, 331)
        pyautogui.click()
    elif keyboard.read_key() == '*':
        # Dispositions as No Answer
        print("No Answer")
        pyautogui.moveTo(1026, 384)
        pyautogui.click()
    elif keyboard.read_key() == '/':
        # Dispositions as Disconnected
        print("Disconnected")
        pyautogui.moveTo(722, 502)
        pyautogui.click()
    return


def HangUp():
    print("Hanging Up...")
    pyautogui.moveTo(177, 565)
    print("\nFor Disposition, press 'del'")
    pyautogui.click()

    keyboard.wait('del')
    Disposition()

    return


def DialNext():
    print("Dialing Next...")
    pyautogui.moveTo(188, 225)
    print("\nWaiting on '-' to hangup")
    pyautogui.click()

    keyboard.wait('-')
    HangUp()
    return


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
        else:
            print("Invalid Operation")


if __name__ == "__main__":
    main()
