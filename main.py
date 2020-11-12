import sys
import os
import glob

from mouse_logger import MouseLogger
from keyboard_logger import KeyboardLogger
from screenshot_taker import ScreenshotTaker


mouseLogger = MouseLogger()
keyLogger =  KeyboardLogger()
screenshotTaker = ScreenshotTaker()

def start_logger():
    mouseLogger.start()
    keyLogger.start()
    screenshotTaker.start()

def main(argv):
    action = argv[0]

    if action == 'start':
        start_logger()

    elif action == 'clean':
        file_list = glob.glob('./log/*')
        file_list.extend(glob.glob('./img/*'))
        for file_path in file_list:
            try:
                os.remove(file_path)
            except:
                print("Error while deleting file : ", file_path)
    else:
        raise ValueError('wrong running option')


if __name__ == "__main__":
    main(sys.argv[1:])