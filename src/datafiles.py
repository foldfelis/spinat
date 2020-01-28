import pandas as pd
import numpy as np


def read_expr(file, col_names, skip_row=0, sep=" "):
    lines = read_file(file, skip_row)
    df = parse2df(lines, col_names, sep)

    return df


def read_file(file, skip_row):
    lines = open(file, "r").readlines()
    lines = lines[skip_row:]

    return lines


def parse2df(lines, col_names, sep):
    for i, line in enumerate(lines):
        line = line.strip().split(sep)
        line = filter(lambda val: val != "", line)
        line = list(map(float, line))
        lines[i] = line

    arr = np.array(lines)
    df = pd.DataFrame(arr[:, :len(col_names)], columns=col_names)

    return df
