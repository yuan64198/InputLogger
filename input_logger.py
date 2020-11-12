import threading
import json

import utils

from Log import Log, Record
from constants import DEFAULT_LOG_MODE, LOG_DIR

class InputLogger(threading.Thread):
    def __init__(self, time_interval=10):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self.interval = time_interval
        self.log = Log()

    def add_record(self, button, is_on_press, coordinates=[0.0,0.0]):
        ts = utils.getTimeStamp()
        record = Record(timestamp=ts, button=button, is_on_press=is_on_press, coordinates=coordinates)
        self.log.append_log(record)

    def save_log(self, filename, mode=DEFAULT_LOG_MODE):

        if mode == 'json':
            filename = self.generate_filename(filename, mode)
            self.save_json(filename)
        elif mode == 'text':
            filename = self.generate_filename(filename, mode)
            self.save_text(filename)
        else:
            raise ValueError('No such log option')

        self.clear_buffer()


    def generate_filename(self, filename, mode):
        if mode == 'json':
            extension = '.json'
        elif mode == 'text':
            extension = '.txt'
        else:
            raise ValueError('Option error for filename generation')

        ts = utils.getTimeStamp()
        filename = filename + '_' + ts + extension
        
        return filename


    def save_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.log.to_json(), json_file)

    def save_text(self, filename):
        with open(filename, "w") as text_file:
            text_file.write(str(self.log))

    def clear_buffer(self):
        self.log = Log()
    
    def save_log_every_timeframe(self, filename, mode=DEFAULT_LOG_MODE):
        threading.Timer(self.interval, self.save_log_every_timeframe, [filename]).start()
        self.save_log(LOG_DIR + filename, mode)
    
    
    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    