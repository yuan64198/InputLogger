import threading

import pyscreenshot as ImageGrab
from PIL import Image

from utils import get_timestamp, print_message
from constants import (IMAGE_DIR, 
                    SCREENSHOT_INTERVAL,
                    SCREENSHOT_FILENAME,
                    IMAGE_WIDTH, 
                    IMAGE_RESIZE)


class ScreenshotLogger(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def take_screenshot(self):
        screenshot = self.get_image()
        self.save_image(screenshot)
        

    
    def take_screenshot_every_timeframe(self):
        threading.Timer(SCREENSHOT_INTERVAL, self.take_screenshot_every_timeframe).start()
        self.take_screenshot()


    def save_image(self, screenshot):
        filename = SCREENSHOT_FILENAME + "_" + get_timestamp() + ".png"
        if IMAGE_RESIZE:
            screenshot = self.resize_image(screenshot)
        screenshot.save(IMAGE_DIR+filename)

        print_message("Save Screenshot to " + IMAGE_DIR+filename)



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
        print_message("===== Start Recording Screenshot =====")
        self.take_screenshot_every_timeframe()

