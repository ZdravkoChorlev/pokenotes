from pynput.keyboard import Listener, Key, KeyCode
from gui import GetNoteText
from utils import save_note


def on_press(key):
    try:
        if key.char == 'r':
            text = GetNoteText()
            filename = ".pokenotes"
            save_note(filename, text)
    except Exception as ex:
        print('Error:', ex)


def on_release(key):
    if key == Key.esc or key == KeyCode.from_char('r'):
        return False


if __name__ == '__main__':
    # Collect events until released
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
