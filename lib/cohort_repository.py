from lib.cohort import Cohort
from lib.student import Student

'''
cohort_id (serial)      cohort_name (text)    starting date (date)
'''

class cohortRepository():
        def __init__(self, connection):
            self._connection = connection

        # Retrieve all cohort
        def all(self):
            print("Starting all method.")
            rows = self._connection.execute('SELECT * from cohorts')
            cohort = []
            print("My cohort is: ", cohort)
            for row in rows:
                print("Looking at a row...")
                item = Cohort(row["cohort_id"], row["cohort_name"], row["date"])
                cohort.append(item)
                print("My cohort is: ", cohort)
            return cohort
        
        def find_with_students(self, cohort_id):
            rows = self._connection.execute(
                "SELECT cohorts.id, cohorts.cohort_name, cohorts.date, students.id AS student_id, students.student_name, students.cohort_id " \
                "FROM cohorts JOIN students ON cohorts.id = students.cohort_id " \
                "WHERE cohorts.id = %s", [cohort_id])
            students = []
            print(rows)
            for row in rows:
                student = Student(row["student_id"], row["student_name"], row["cohort_id"])
                students.append(student)

            # Each row has the same id, name, and genre, so we just use the first
            return Cohort(rows[0]["cohort_id"], rows[0]["cohort_name"], rows[0]["date"], students)