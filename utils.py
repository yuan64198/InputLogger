import datetime

def getTimeStamp():
    now = datetime.datetime.now()
    ts = now.strftime('%Y%m%d_%H%M%S')
    return ts

def print_message(msg):
    ts = getTimeStamp()
    print("[" + ts + "]: " + msg)