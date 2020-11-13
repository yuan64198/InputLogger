import json

from utils import getTimeStamp


class Log:

    def __init__(self):
        self.timestamp = getTimeStamp()
        self.records = []

    def __str__(self):
        string = ''
        for record in self.records:
            string += str(record) + '\n'
        return string

    def append_log(self, record):
        self.records.append(record)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)



class Record:

    def __init__(self, timestamp, button, is_on_press, coordinates):
        self.timestamp = timestamp
        self.button = button
        self.is_on_press = is_on_press
        self.coordinates = coordinates
        
        
    def __str__(self):

        string = self.timestamp + '    ' + self.button + ' '
        if self.is_on_press:
            string += 'pressed    '
        else:
            string += 'released    '
        
        string += str(int(self.coordinates[0])) + ',' + str(int(self.coordinates[1]))

        return string