"""Reading the marks from a CSV file."""

import csv

import numpy as np


def load_grades(path):
    """Read a CSV file of marks.

    The file must look like this (first line = column names):

        student,maths,physics
        Anna,78,82
        Ben,55,60

    Parameters
    ----------
    path : str or pathlib.Path
        Where the CSV file is.

    Returns
    -------
    students : list of str
        The names of the students (first column).
    subjects : list of str
        The names of the subjects (the other column names).
    marks : numpy.ndarray
        A table of numbers. Each ROW is one student and each COLUMN is one
        subject, in the same order as `students` and `subjects`.
    """
    students = []
    rows_of_marks = []

    with open(path, newline="") as file:
        reader = csv.reader(file)

        header = next(reader)       # the first line holds the column names
        subjects = header[1:]       # everything except the "student" column

        for row in reader:
            if len(row) == 0:       # ignore empty lines
                continue
            students.append(row[0])                           # the name
            rows_of_marks.append([float(x) for x in row[1:]])  # the marks

    # Turn the list of lists into a NumPy table so we can calculate with it.
    marks = np.array(rows_of_marks)
    return students, subjects, marks
