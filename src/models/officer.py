from datetime import datetime

class Officer:

    def __init__(self, employe_id: str,  dob: datetime, salary: float, name: str = None):

        self.employe_id = employe_id
        self.name = name
        self.dob = dob
        self.__salary = salary


    def __lt__(self, another_officer: 'Officer'):

        return self.employe_id < another_officer.employe_id
        


    def __str__(self):

        return f"employe_id: {self.employe_id}\nname: {self.name}\n"
    


