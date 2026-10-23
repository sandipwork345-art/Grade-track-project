"""Bar charts of the marks."""

import matplotlib.pyplot as plt


def plot_student_averages(averages, pass_mark=50):
    """Draw one bar per student showing their average mark.

    A dashed red line shows the pass mark. Bars below the line are drawn in
    red, the others in green.

    Parameters
    ----------
    averages : dict
        The result of student_averages().
    pass_mark : float, optional
        Where to draw the red line.

    Returns
    -------
    tuple
        The Matplotlib figure and axes.
    """
    names = list(averages.keys())
    values = list(averages.values())

    # Choose a colour for every bar: red if failing, green if passing.
    colours = []
    for value in values:
        if value < pass_mark:
            colours.append("tomato")
        else:
            colours.append("seagreen")

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(names, values, color=colours)
    ax.axhline(pass_mark, color="red", linestyle="--", label="pass mark")

    ax.set_title("Average mark per student")
    ax.set_ylabel("average mark")
    ax.set_ylim(0, 100)
    ax.legend()
    fig.tight_layout()
    return fig, ax


def plot_subject_averages(averages):
    """Draw one bar per subject showing the class average.

    Parameters
    ----------
    averages : dict
        The result of subject_averages().

    Returns
    -------
    tuple
        The Matplotlib figure and axes.
    """
    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.bar(list(averages.keys()), list(averages.values()), color="steelblue")

    ax.set_title("Class average per subject")
    ax.set_ylabel("average mark")
    ax.set_ylim(0, 100)
    fig.tight_layout()
    return fig, ax
