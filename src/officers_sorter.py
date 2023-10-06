from models.officer import Officer
from datetime import datetime as dtm

officers_list = [
    Officer("30", dtm.now(),50.0,"Employe 1"),
    Officer("10", dtm.now(),50.0,"Employe 2"),
    Officer("25", dtm.now(),50.0,"Employe 3"),
    Officer("7", dtm.now(),50.0,"Employe 4"),
]

officers_list.sort()
for officer in officers_list:
    print(officer)
