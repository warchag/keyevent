from pynput.keyboard import Listener
from ClassEvent import *

if __name__ == "__main__":    
    mykey = KeyboardEvent()
    with Listener(
            on_press=mykey.on_press,
            on_release=mykey.on_release) as listener:
        listener.join()
