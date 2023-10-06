import pandas as pd
from datetime import datetime, tzinfo, timedelta
from zoneinfo import ZoneInfo

from models.shift import Shift

#Shifts timezone (-07:00)
work_time_zone = ZoneInfo("America/Los_Angeles")

"""
    shift_mapper:

        This function takes a shift record from the pandas DataFrame
        and map it to a model class 'Shift'

        Returns an instance of the 'Shift' populated with the data sotored 
        in the provided DataFrame record
"""
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


"""
    filter_extra_time_shifts:

        This function is a filter to extract those shifts
        from an 'Shift's list that last more than 8 hours.

        Returns True if the input Shift last more than 8 hours
    
"""
def filter_extra_time_shifts(shift: Shift):

    if(shift.duration > 8):
        shift.cut_extra_time = (shift.start_timestamp + timedelta(hours=8)).replace(tzinfo=work_time_zone)
        return True

"""
    is_graveyard:

        This function indicates if a Shift cross the midnight

        Returns True if the start time day is lower than the end time day
"""
def is_graveyard(shift: Shift):
    
   return(shift.start_timestamp.day < shift.end_timestamp.day)
    
    
#Reading the data input data from shifts.csv
shifts_data = pd.read_csv("shifts.csv")

#Selecting the relevant columns
shifts_list = shifts_data[
    ["bubo_shift_id", "bubo_employee_id", "start_timestamp", "end_timestamp"]
].to_dict(orient="records")

#Shift mapping from DataFrame to model list
shifts_models_list = list(map(shift_mapper, shifts_list))

#Obtaining those shifts that last more than 8 hrs
extra_time_shifts = list(filter(filter_extra_time_shifts,shifts_models_list))

print("The following shifts are grater than 8 hrs:")

#Printing those shifts that last more than 8 hrs and it is indicate
#if the shift cross the midnight
for shift in extra_time_shifts:
    shift_is_graveyard = is_graveyard(shift)
    print(f"Shift: {'[is graveyard]' if shift_is_graveyard else ''}")
    print(shift)
    print(f"Extra hours: From {shift.cut_extra_time} to {shift.end_timestamp} ({shift.duration - 8}hrs)\n")
    
