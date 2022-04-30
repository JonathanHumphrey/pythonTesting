
import pyautogui
import keyboard


def Disposition():
    print("Select a Disposition for the call: \nAns. Mach. = 1\nNo Answer = 2\nDisconnected = 3\nCall Back = 4\nBusy = 5")
    keyboard.read_key()

    invalid = True
    while invalid:
        if keyboard.read_key() == '1':
            # Dispositions as Answering Machine
            pyautogui.moveTo(689, 315)
            print("Answering Machine")
            pyautogui.doubleClick()
            invalid = False
        elif keyboard.read_key() == '2':
            # Dispositions as No Answer
            pyautogui.moveTo(1026, 384)
            print("No Answer")
            pyautogui.doubleClick()
            invalid = False
        elif keyboard.read_key() == '3':
            # Dispositions as Disconnected
            pyautogui.moveTo(722, 502)
            print("Disconnected")
            pyautogui.doubleClick()
            invalid = False
        elif keyboard.read_key == '4':
            pyautogui.moveTo(694, 425)
            print("Call Back")
            pyautogui.doubleClick()
            invalid = False
        elif keyboard.read_key == '5':
            pyautogui.moveTo(619, 351)
            print("Busy")
            pyautogui.doubleClick()
            invalid = False
        else:
            print(
                "Enter a valid number: \nAns. Mach. = 1\nNo Answer = 2\nDisconnected = 3\nCall Back = 4\nBusy = 5")
    return


def HangUp():
    print("Hanging Up...")
    pyautogui.moveTo(199, 538)
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
