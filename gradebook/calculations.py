"""The calculations on the marks.

All functions use the same three things that load_grades returns:
    students  - list of names
    subjects  - list of subject names
    marks     - NumPy table, one row per student, one column per subject
"""

import numpy as np


def student_averages(students, marks):
    """Calculate the average mark of every student.

    Returns
    -------
    dict
        {student name: average mark}, for example {"Anna": 75.0}.
    """
    # axis=1 means "average along each row", so we get one number per student.
    averages = np.mean(marks, axis=1)

    result = {}
    for name, average in zip(students, averages):
        result[name] = float(average)
    return result


def subject_averages(subjects, marks):
    """Calculate the average mark of every subject (the class average).

    Returns
    -------
    dict
        {subject name: average mark}, for example {"maths": 67.9}.
    """
    # axis=0 means "average down each column", so we get one number per subject.
    averages = np.mean(marks, axis=0)

    result = {}
    for subject, average in zip(subjects, averages):
        result[subject] = float(average)
    return result


def best_student(averages):
    """Find the student with the highest average.

    Parameters
    ----------
    averages : dict
        The result of student_averages().

    Returns
    -------
    tuple
        (name, average) of the best student.
    """
    best_name = None
    best_average = -1.0
    for name, average in averages.items():
        if average > best_average:      # found someone better, remember them
            best_name = name
            best_average = average
    return best_name, best_average


def letter_grade(average):
    """Turn an average mark (0-100) into a letter.

    80 or more = A, 70 or more = B, 60 or more = C, 50 or more = D,
    anything lower = F.
    """
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def marks_below_pass(students, subjects, marks, pass_mark=50):
    """Find every single mark that is below the pass mark.

    This shows which students need help, and in which subject.

    Returns
    -------
    list of tuple
        Each item is (student, subject, mark).
    """
    problems = []
    for row, student in enumerate(students):         # go through each student
        for column, subject in enumerate(subjects):  # and each of their subjects
            mark = float(marks[row, column])
            if mark < pass_mark:
                problems.append((student, subject, mark))
    return problems
