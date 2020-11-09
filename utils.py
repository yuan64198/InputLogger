import datetime

def getTimeStamp():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%dT%H:%M:%S') + ('-%02d' % (now.microsecond / 10000))
    return ts