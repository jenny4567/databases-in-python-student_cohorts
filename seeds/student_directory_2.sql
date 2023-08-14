DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name text,
  date text
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (id, cohort_name, date) VALUES (1,'this cohort', '2023-05-12');
INSERT INTO cohorts (id, cohort_name, date) VALUES (2,'that cohort', '2023-05-12');
INSERT INTO cohorts (id, cohort_name, date) VALUES (3, 'third cohort', '2023-05-12');

INSERT INTO students (id,student_name, cohort_id) VALUES (1,'Tony Stark', 1);
INSERT INTO students (id,student_name, cohort_id) VALUES (2,'Natasha Romanov', 1);
INSERT INTO students (id,student_name, cohort_id) VALUES (3,'Magneto', 2);
INSERT INTO students (id,student_name, cohort_id) VALUES (4,'Professor X', 3);
INSERT INTO students (id,student_name, cohort_id) VALUES (5,'Steve Rogers', 1);
