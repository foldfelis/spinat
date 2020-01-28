import pandas as pd
import numpy as np


def file2df(file, col_names, skip_row=0, sep=" "):
    lines = file2lines(file, skip_row)
    df = lines2df(lines, col_names, sep)

    return df


def file2lines(file, skip_row=0):
    lines = open(file, "rb").readlines()
    lines = lines[skip_row:]
    return lines


def lines2df(lines, col_names, sep=" "):
    for i, line in enumerate(lines):
        line = line.strip().split(sep)
        line = filter(lambda val: val != "", line)
        line = list(map(float, line))
        lines[i] = line

    arr = np.array(lines)
    df = pd.DataFrame(arr[:, :len(col_names)], columns=col_names)

    return df
