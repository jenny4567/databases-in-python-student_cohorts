from lib.student import Student

'''
id(SERIAL)      name(text)    cohort id(int)
'''

def test_student_constructs():
    student1 = Student(1, 'my name', 'my cohort')

    assert student1.id == 1
    assert student1.student_name == 'my name'
    assert student1.cohort_id == 'my cohort'

def test_equlity():
    student1 = Student(1, 'my name', 'my cohort')
    student2 = Student(1, 'my name', 'my cohort')
    assert student1 == student2

def test_print_format():
    student1 = Student(1, 'my name', 'my cohort')
    assert str(student1) == "1 - my name - my cohort"