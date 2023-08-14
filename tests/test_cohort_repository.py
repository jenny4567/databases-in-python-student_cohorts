from lib.cohort_repository import cohortRepository
from lib.cohort import Cohort
from lib.student import Student
from datetime import datetime

"""
When we call cohortRepository#all
We get a list of cohort objects reflecting the seed data.
"""

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = cohortRepository(db_connection)
    cohort = repository.find_with_students(1)
    assert cohort == Cohort(1, 'this cohort', '2023-05-12', [
        Student(1, "Tony Stark", 1),
        Student(2, "Natasha Romanov", 1),
        Student(5, "Steve Rogers", 1)
    ])