import threading

import pyscreenshot as ImageGrab
from PIL import Image

import utils
from input_logger import InputLogger
from constants import (IMAGE_DIR, SCREENSHOT_INTERVAL, IMAGE_WIDTH, IMAGE_RESIZE)


class ScreenshotTaker(InputLogger):
    def __init__(self):
        super().__init__()
        print("===== Screenshot Started =====")


    def take_screenshot(self):
        screenshot = self.get_image()
        self.save_image(screenshot)
        print("===== Take Screenshot =====")

    
    def take_screenshot_every_timeframe(self):
        threading.Timer(SCREENSHOT_INTERVAL, self.take_screenshot_every_timeframe).start()
        self.take_screenshot()


    def save_image(self, screenshot):
        filename = "ScreenShot_" + utils.getTimeStamp() + ".png"
        if IMAGE_RESIZE:
            screenshot = self.resize_image(screenshot)
        screenshot.save(IMAGE_DIR+filename)



    def get_image(self):
        screenshot = ImageGrab.grab()
        return screenshot


    def resize_image(self, im):
        width = IMAGE_WIDTH
        width_ratio = (width/float(im.size[0]))
        height = int((float(im.size[1])*float(width_ratio)))
        im = im.resize((width,height), Image.ANTIALIAS)
        return im


    def run(self):
        self.take_screenshot_every_timeframe()

