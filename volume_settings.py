from time import sleep
from pynput.keyboard import Key, Controller

kb=Controller()  
def volume_up():
    for i in range(2):
        kb.press(Key.media_volume_up)
        kb.release(Key.media_volume_up)
        sleep(0.1)

def volume_down():
    for i in range(2):
        kb.press(Key.media_volume_down)
        kb.release(Key.media_volume_down)
        sleep(0.1)

