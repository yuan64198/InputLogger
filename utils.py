import datetime

def getTimeStamp():
    now = datetime.datetime.now()
    ts = now.strftime('%Y%m%d_%H%M%S')
    return ts