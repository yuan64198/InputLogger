from constants import LOG_DIR, MOUSE_LOG_ON_RELEASE
from pynput import mouse

from input_logger import InputLogger
from constants import (LOG_DIR, MOUSE_LOG_INTERVAL, MOUSE_LOG_ON_PRESS)

class MouseLogger(InputLogger):
    def __init__(self):
        super().__init__(MOUSE_LOG_INTERVAL)
        self.log += "=====MouseLogger Started====="
    
    def on_move(self, x, y):
        pass

    def on_scroll(self, x, y, dx, dy):
        pass

    def on_click(self, x, y, button, pressed):
        if(pressed == True and MOUSE_LOG_ON_PRESS):
            log = str(button) + " pressed at " + "({},{})".format(x,y)
            self.add_log(log)
        if(pressed == False and MOUSE_LOG_ON_RELEASE):
            log = str(button) + " release at " + "({},{})".format(x,y)
            self.add_log(log)
   
    def run(self):
        self.save_log(LOG_DIR + 'mouse_log.txt')
        mouse_listener = mouse.Listener(
        on_move=self.on_move,
        on_click=self.on_click,
        on_scroll=self.on_scroll)
        
        with mouse_listener:
            mouse_listener.join()
