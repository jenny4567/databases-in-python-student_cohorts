from lib.cohort import Cohort
from datetime import datetime

'''
id(SERIAL)      name(text)    cohort id(int)
'''

def test_cohort_constructs():
    date_today = datetime.today().strftime('%Y-%m-%d')
    cohort1 = Cohort(1, 'my name', date_today)
    assert cohort1.id == 1
    assert cohort1.cohort_name == 'my name'
    assert cohort1.date == datetime.today().strftime('%Y-%m-%d')

def test_equlity():
    date_today1 = datetime.today().strftime('%Y-%m-%d')
    date_today2 = '2023-05-12'
    cohort1 = Cohort(1, 'my name', date_today1)
    cohort2 = Cohort(1, 'my name', date_today2)
    assert cohort1 == cohort2

def test_print_format():
    date_today = datetime.today().strftime('%Y-%m-%d')
    cohort1 = Cohort(1, 'my name', date_today, 'students')
    assert str (cohort1) == f"1 - my name - {date_today} - students"