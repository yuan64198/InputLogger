
ENABLE_KEYBOARD = True
ENABLE_MOUSE = True
ENABLE_SCREENSHOT = True
ENABLE_AUDIO = True




##### Log #####
DEFAULT_LOG_MODE = 'json'




##### Mouse Logger #####

# Time interval for input logging and screenshot
MOUSE_LOG_FILENAME = 'mouse_log'

MOUSE_LOG_INTERVAL = 10

MOUSE_LOG_ON_PRESS = True

MOUSE_LOG_ON_RELEASE = True





##### Keyboard Logger #####
KEYBOARD_LOG_FILENAME = 'keyboard_log'

KEYBOARD_LOG_INTERVAL = 10

KEYBOARD_LOG_ON_PRESS = True

KEYBOARD_LOG_ON_RELEASE = True





##### Screenshot Logger #####
SCREENSHOT_FILENAME = 'screenshot'

SCREENSHOT_INTERVAL = 2

IMAGE_RESIZE = False

IMAGE_WIDTH = 800



##### Audio Logger #####
AUDIO_LOG_FILENAME = 'audio_log'

CHUNK = 1024

NUM_CHANNEL = 1

FS = 44100

AUDIO_LOG_INTERVAL = 10



# The expected running time for the program
PROGRAM_LIFETIME = 3





# Time interval for checking if any file under the folder is opened
FILE_CHECKING_INTERVAL = 1




AUDIO_DIR = './audio/'

IMAGE_DIR = './img/'

LOG_DIR = './log/'