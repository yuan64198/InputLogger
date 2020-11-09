import datetime
import threading

class InputLogger(threading.Thread):
    def __init__(self, time_interval):
        threading.Thread.__init__(self)
        self.interval = time_interval
        self.log = ""

    def add_log(self, line):
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%dT%H:%M:%S') + ('-%02d' % (now.microsecond / 10000))
        self.log += ts + "    " + line + "\n"
        

    def save_log(self, file_name):
        threading.Timer(self.interval, self.save_log, [file_name]).start()
        f = open(file_name, "a")
        f.write(self.log)
        f.close()
        print(self.log)
        self.log = ""

    