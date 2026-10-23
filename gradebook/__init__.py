"""gradebook: a small package to look at the marks of a class.

What it can do:
    load_grades            read the marks from a CSV file
    student_averages       average mark of every student
    subject_averages       average mark of every subject
    best_student           who has the highest average
    letter_grade           turn an average into a letter (A, B, C, D, F)
    marks_below_pass       find every mark that is below the pass mark
    plot_student_averages  bar chart of the students
    plot_subject_averages  bar chart of the subjects
"""

from .loader import load_grades
from .calculations import (student_averages, subject_averages, best_student,
                           letter_grade, marks_below_pass)
from .charts import plot_student_averages, plot_subject_averages

__all__ = [
    "load_grades",
    "student_averages",
    "subject_averages",
    "best_student",
    "letter_grade",
    "marks_below_pass",
    "plot_student_averages",
    "plot_subject_averages",
]
