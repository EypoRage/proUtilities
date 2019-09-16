import pynput
from pynput import keyboard

def on_press(key):
    try:
        print('Key {0} pressed'.format(key.char))
        #Add your code to drive motor
    except AttributeError:
        print('Key {0} pressed'.format(key))
        #Add Code
def on_release(key):
    print('{0} released'.format(key))
    #Add your code to stop motor
    if key == keyboard.Key.esc:
        # Stop listener
        # Stop the Robot Code
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()