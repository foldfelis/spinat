import pandas as pd
import numpy as np


def file2lines(fn):
    lines = []
    with open(fn, "r") as f:
        for line in f:
            lines.append(line)

    return lines


def remove_header(lines, n_line):
    for i in range(n_line):
        lines.pop(0)

    return lines


def lines2array(lines, sep=" "):
    for i, line in enumerate(lines):
        line = line.split(sep)
        line = [
            float(val)
            for val in line
            if val != "" and val != "\n"
        ]
        lines[i] = line

    arr = np.array(lines)

    return arr


def array2df(arr, col_names):
    df = pd.DataFrame(arr, columns=col_names)

    return df
