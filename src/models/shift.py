from datetime import datetime
class Shift:

    def __init__(self, shift_id: str, start_timestamp: datetime, end_timestamp: datetime, employe_id: str):

        self.shift_id = shift_id
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.employe_id = employe_id
        self.duration = ((self.end_timestamp - self.start_timestamp).seconds) / 3600
        self.cut_extra_time = None

    def __str__(self):

        return f"shift_id: {self.shift_id}, \nemploye_id: {self.employe_id}, \nstart_time: {self.start_timestamp}, \nend_time: {self.end_timestamp}"