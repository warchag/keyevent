from pynput.keyboard import Listener
from ClassEvent import *
from ClassGui import *


if __name__ == "__main__":    
    Main = Gui()
    Main.Draw_Gui()
    #mykey = KeyboardEvent()
    #with Listener(
     #       on_press=mykey.on_press,
      #      on_release=mykey.on_release) as listener:
       # listener.join()
