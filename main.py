import sys
import os
import glob

from mouse_logger import MouseLogger
from keyboard_logger import KeyboardLogger
from screenshot_logger import ScreenshotLogger
from audio_logger import AudioLogger
from constants import (ENABLE_KEYBOARD,
                    ENABLE_MOUSE,
                    ENABLE_SCREENSHOT,
                    ENABLE_AUDIO,)



def main(argv):
    action = argv[0]

    if action == 'start':
        start_logger()

    elif action == 'clean':
        clean_log()
    else:
        raise ValueError('wrong running option')


def start_logger():
    if ENABLE_KEYBOARD:
        MouseLogger().start()
    if ENABLE_KEYBOARD:
        KeyboardLogger().start()
    if ENABLE_SCREENSHOT:
        ScreenshotLogger().start()
    if ENABLE_AUDIO:
        AudioLogger().start()


def clean_log():
    file_list = glob.glob('./log/*')
    file_list.extend(glob.glob('./img/*'))
    for file_path in file_list:
        try:
            os.remove(file_path)
        except:
            print("Error while deleting file : ", file_path) 



if __name__ == "__main__":
    main(sys.argv[1:])