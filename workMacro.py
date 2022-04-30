
import pyautogui
import keyboard


def Disposition():
    print("Select a Disposition for the call: \nAns. Mach. = '-'\nNo Answer = '*'\nDisconnected = '/'\n")
    keyboard.read_key()
    if keyboard.read_key() == '-':
        # Dispositions as Answering Machine
        pyautogui.moveTo(689, 315)
        print("Answering Machine")

        pyautogui.doubleClick()

    elif keyboard.read_key() == '*':
        # Dispositions as No Answer
        pyautogui.moveTo(1026, 384)
        print("No Answer")

        pyautogui.doubleClick()

    elif keyboard.read_key() == '/':
        # Dispositions as Disconnected
        pyautogui.moveTo(722, 502)
        print("Disconnected")

        pyautogui.doubleClick()
    elif keyboard.read_key() == 'enter':
        # Opens Call Back menu
        pyautogui.moveTo(694, 425)
        print("Call Back")

        pyautogui.doubleClick()
    elif keyboard.read_key() == 'insert':
        # Dispositions as Busy
        pyautogui.moveTo(619, 351)
        print("Busy")

        pyautogui.doubleClick()

    return


def HangUp():
    print("Hanging Up...")
    pyautogui.moveTo(177, 565)
    print("\nFor Disposition, press 'del'")
    pyautogui.click()

    keyboard.wait('del')
    Disposition()


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
    print("\nPress + to Dial\nPress * to quit\n")
    while loopTracker:
        keyboard.read_event()

        if keyboard.is_pressed('+'):
            DialNext()
        elif keyboard.is_pressed('*'):
            loopTracker = False
        else:
            print("\nPress + to Dial\nPress * to quit\n")


if __name__ == "__main__":
    main()
