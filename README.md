# gradebook

A small Python package that turns a table of student marks into useful answers.

A teacher usually has a spreadsheet of marks and wants to know things like:
who is doing best, how the class did in each subject, and who needs help.
`gradebook` reads a CSV file of marks and answers these questions with simple
calculations and charts.

It uses **only** the Python Standard Library, NumPy and Matplotlib.

## Project structure

```
grade_tracker/
|-- README.md
|-- pyproject.toml
|-- gradebook/             # the package
|   |-- __init__.py
|   |-- loader.py          # load_grades
|   |-- calculations.py    # averages, best student, letter grades, marks below pass
|   |-- charts.py          # the two bar charts
|-- demo/
|   |-- demo01_class_report.py
|-- data/
    |-- grades.csv
```

## Installation

You need Python 3.8 or newer.

```bash
git clone https://github.com/<your-username>/grade_tracker.git
cd grade_tracker
pip install -e .
```

This installs the package together with NumPy and Matplotlib. The demo also works
without installing the package, as long as NumPy and Matplotlib are installed
(`pip install numpy matplotlib`).

## The data file

`data/grades.csv` has one line per student. The first line holds the column names:

```
student,maths,physics,english
Anna,78,82,65
Ben,55,60,72
```

The first column is the student's name; every other column is a subject with marks
from 0 to 100. You can add students or subjects, or use your own file in the same format.
The marks in the example file are made up.

## How to use the main functions

```python
from gradebook import (load_grades, student_averages, subject_averages,
                       best_student, letter_grade, marks_below_pass)

# Read the file. "marks" is a table: one row per student, one column per subject.
students, subjects, marks = load_grades("data/grades.csv")

averages = student_averages(students, marks)     # {"Anna": 75.0, ...}
print(best_student(averages))                    # ("Chloe", 86.0)
print(letter_grade(averages["Anna"]))            # "B"
print(subject_averages(subjects, marks))         # {"maths": 67.1, ...}
print(marks_below_pass(students, subjects, marks, pass_mark=50))
```

| Function | What it does |
|----------|--------------|
| `load_grades(path)` | Reads the CSV file and returns the students, the subjects and the table of marks. |
| `student_averages(students, marks)` | Average mark of each student (average along each row). |
| `subject_averages(subjects, marks)` | Average mark of each subject (average down each column). |
| `best_student(averages)` | Name and average of the student with the highest average. |
| `letter_grade(average)` | A (80+), B (70+), C (60+), D (50+) or F. |
| `marks_below_pass(students, subjects, marks, pass_mark=50)` | Every mark below the pass mark, as `(student, subject, mark)`. |
| `plot_student_averages(averages, pass_mark=50)` | Bar chart of the students; red bars are below the pass mark. |
| `plot_subject_averages(averages)` | Bar chart of the class average per subject. |

Every function has a docstring: use `help(gradebook.student_averages)` to read it.

## Running the demonstration

From the root directory:

```bash
python demo/demo01_class_report.py
```

The demo loads the example file, prints each student's average and letter grade,
the best student, the class average per subject and the marks below 50, and then
opens two bar charts on screen (close the chart windows to finish). The top of the
demo file explains each step.

## How it works (in short)

The marks are stored in a NumPy table with one row per student and one column per
subject. Taking the average along the rows (`axis=1`) gives one average per student,
and taking it down the columns (`axis=0`) gives one average per subject. Everything else
is a simple loop that goes through the students and compares numbers.
