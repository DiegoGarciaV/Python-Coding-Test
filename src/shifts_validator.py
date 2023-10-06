import pandas as pd
from datetime import datetime, tzinfo, timedelta
from zoneinfo import ZoneInfo

from models.shift import Shift


work_time_zone = ZoneInfo("America/Los_Angeles")


def shift_mapper(shift_record):
    init_time = datetime.fromisoformat(shift_record["start_timestamp"]).replace(
        tzinfo=work_time_zone
    )

    end_time = datetime.fromisoformat(shift_record["end_timestamp"]).replace(
        tzinfo=work_time_zone
    )

    return Shift(
        shift_id=shift_record["bubo_shift_id"],
        employe_id=shift_record["bubo_employee_id"],
        start_timestamp=init_time,
        end_timestamp=end_time,
    )

def filter_extra_time_shifts(shift: Shift):

    if(shift.duration > 8):
        shift.cut_extra_time = (shift.start_timestamp + timedelta(hours=8)).replace(tzinfo=work_time_zone)
        return True

def is_graveyard(shift: Shift):
    
   return(shift.start_timestamp.day < shift.end_timestamp.day)
    
    

shifts_data = pd.read_csv("shifts.csv")
shifts_list = shifts_data[
    ["bubo_shift_id", "bubo_employee_id", "start_timestamp", "end_timestamp"]
].to_dict(orient="records")

shifts_models_list = list(map(shift_mapper, shifts_list))

extra_time_shifts = list(filter(filter_extra_time_shifts,shifts_models_list))

print("The following shifts are grater than 8 hrs:")

for shift in extra_time_shifts:
    shift_is_graveyard = is_graveyard(shift)
    print(f"Shift: {'[is graveyard]' if shift_is_graveyard else ''}")
    print(shift)
    print(f"Extra hours: From {shift.cut_extra_time} to {shift.end_timestamp} ({shift.duration - 8}hrs)\n")
