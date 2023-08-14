'''
cohort_id (serial)      cohort_name (text)    starting date (date)
'''

class Cohort():
    def __init__(self, id, cohort_name, date, students = None):
        self.id = id
        self.cohort_name = cohort_name
        self.date = date
        self.students = students or []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id} - {self.cohort_name} - {self.date} - {self.students}"
    
    