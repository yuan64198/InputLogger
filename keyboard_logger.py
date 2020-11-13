from pynput import keyboard

from utils import print_message
from input_logger import InputLogger
from constants import (KEYBOARD_LOG_INTERVAL, 
                    KEYBOARD_LOG_ON_PRESS, 
                    KEYBOARD_LOG_ON_RELEASE,
                    KEYBOARD_LOG_FILENAME,)



class KeyboardLogger(InputLogger):


    def __init__(self):
        super().__init__(KEYBOARD_LOG_INTERVAL)
        


    def parse_key(self, key):
        try:
            keyStr = str(key.char)
        except AttributeError:
            if key == key.space:
                keyStr = "SPACE"
            elif key == key.esc:
                keyStr = "ESC"
            elif key == key.shift:
                keyStr = "SHIFT"
            elif key == key.tab:
                keyStr = "TAB"
            elif key == key.enter:
                keyStr = "ENTER"
            else:
                keyStr = " " + str(key) + " "
        return keyStr


    def on_press(self, key):
        if KEYBOARD_LOG_ON_PRESS == False:
            return
        keyStr = self.parse_key(key)
        log = str(keyStr)
        self.add_record(log, is_on_press=True)


    def on_release(self, key):
        if KEYBOARD_LOG_ON_RELEASE == False:
            return
        keyStr = self.parse_key(key)
        log = str(keyStr)
        self.add_record(log, is_on_press=False)
    
        
    def run(self):

        print_message("===== Start Recording Mouse Input =====")

        self.save_log_every_timeframe(KEYBOARD_LOG_FILENAME)
        keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release = self.on_release)
        with keyboard_listener:
            keyboard_listener.join()