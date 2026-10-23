"""Demo: make a report for a class of students.

The problem
-----------
data/grades.csv has the marks of 8 students in 3 subjects. A teacher wants
quick answers to these questions:
  * What is each student's average, and which letter grade is that?
  * Who is the best student?
  * How did the class do in each subject?
  * Which students have a mark below the pass mark (50)?

What this script does, step by step
-----------------------------------
1. Loads the CSV file.
2. Calculates and prints each student's average and letter grade.
3. Finds the best student.
4. Calculates the class average for each subject.
5. Lists the marks that are below the pass mark.
6. Draws two bar charts and shows them on screen.

How to run it (from the root directory)
---------------------------------------
    python demo/demo01_class_report.py
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt

# These two lines let the script find the gradebook package even if it has
# not been installed with pip: they add the root directory to Python's path.
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from gradebook import (best_student, letter_grade, load_grades,
                       marks_below_pass, plot_student_averages,
                       plot_subject_averages, student_averages,
                       subject_averages)

# --- Step 1: load the data ---------------------------------------------------
students, subjects, marks = load_grades(ROOT / "data" / "grades.csv")
print(f"Loaded {len(students)} students and {len(subjects)} subjects: {subjects}\n")

# --- Step 2: average and letter grade of every student -----------------------
averages = student_averages(students, marks)
print("Student averages:")
for name, average in averages.items():
    print(f"  {name:<8} {average:5.1f}   grade {letter_grade(average)}")

# --- Step 3: the best student ------------------------------------------------
name, average = best_student(averages)
print(f"\nBest student: {name} with an average of {average:.1f}\n")

# --- Step 4: class average per subject ---------------------------------------
class_averages = subject_averages(subjects, marks)
print("Class average per subject:")
for subject, average in class_averages.items():
    print(f"  {subject:<8} {average:5.1f}")

# --- Step 5: marks below the pass mark ---------------------------------------
problems = marks_below_pass(students, subjects, marks, pass_mark=50)
print(f"\nMarks below 50 ({len(problems)} found):")
for student, subject, mark in problems:
    print(f"  {student} in {subject}: {mark:.0f}")

# --- Step 6: draw the charts -------------------------------------------------
fig1, ax1 = plot_student_averages(averages, pass_mark=50)
fig2, ax2 = plot_subject_averages(class_averages)

# plt.show() opens both charts in windows on your screen.
# Close the windows to finish the script.
plt.show()
