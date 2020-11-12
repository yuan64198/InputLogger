import threading

import pyscreenshot as ImageGrab

import utils
from input_logger import InputLogger
from constants import (IMAGE_DIR, SCREENSHOT_INTERVAL,)


class ScreenshotTaker(InputLogger):
    def __init__(self):
        super().__init__()
        print("=====Screenshot Started=====")

    def takeScreenshot(self):
        threading.Timer(SCREENSHOT_INTERVAL, self.takeScreenshot).start()
        
        filename = "ScreenShot_" + utils.getTimeStamp() + ".png"
        im = ImageGrab.grab()
        im.save(IMAGE_DIR+filename)

    def run(self):
        self.takeScreenshot()
