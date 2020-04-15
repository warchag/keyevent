from pynput.keyboard import Key, Listener
import subprocess

class KeyboardEvent():
    def on_press(self,key):
        print(f'{key} pressed')
        if str(key) == "'*'":
            subprocess.Popen("explorer.exe")
        if str(key) == "'+'":
            subprocess.Popen("calc1.exe")    
    def on_release(self,key):
        print(f'{key} release')
        if key == Key.esc:
            return False

 

    