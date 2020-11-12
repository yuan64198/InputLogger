from pynput import mouse

from input_logger import InputLogger
from constants import (LOG_DIR, 
                    MOUSE_LOG_INTERVAL, 
                    MOUSE_LOG_ON_PRESS, 
                    MOUSE_LOG_ON_RELEASE,
                    MOUSE_LOG_FILENAME,)

class MouseLogger(InputLogger):
    def __init__(self):
        super().__init__(MOUSE_LOG_INTERVAL)
        print('===== MouaseLogger Started =====') 
    
    def on_move(self, x, y):
        pass

    def on_scroll(self, x, y, dx, dy):
        pass

    def on_click(self, x, y, button, pressed):
        if(pressed == True and MOUSE_LOG_ON_PRESS):
            self.add_record(str(button), is_on_press=True, coordinates=[x, y])
        if(pressed == False and MOUSE_LOG_ON_RELEASE):
            self.add_record(str(button), is_on_press=False, coordinates=[x, y])
   
    def run(self):
        self.save_log_every_timeframe(MOUSE_LOG_FILENAME)
        mouse_listener = mouse.Listener(
        on_move=self.on_move,
        on_click=self.on_click,
        on_scroll=self.on_scroll)
        
        with mouse_listener:
            mouse_listener.join()
