import pandas as pd
import numpy as np


def file2df(fn, col_names, n_header=0, sep=" "):
    lines = file2lines(fn)
    lines = remove_header(lines, n_header)
    arr = lines2array(lines, sep)
    df = array2df(arr, col_names)

    return df


def file2lines(fn):
    lines = []
    with open(fn, "r") as f:
        for line in f:
            lines.append(line)

    return lines


def remove_header(lines, n_header):
    for i in range(n_header):
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
    df = pd.DataFrame(arr[:, :len(col_names)], columns=col_names)

    return df
