import threading
import pyscreenshot as ImageGrab
import utils

IMAGE_DIR = ''

class ScreenshotTaker(threading.Thread):
    def __init__(self, time_interval):
        threading.Thread.__init__(self)
        self.interval = time_interval
        print("=====Screenshot Started=====")

    def takeScreenshot(self):
        threading.Timer(self.interval, self.takeScreenshot).start()
        
        file_name = "ScreenShot_" + utils.getTimeStamp() + ".png"
        im = ImageGrab.grab()
        im.save(file_name)

    def run(self):
        self.takeScreenshot()
