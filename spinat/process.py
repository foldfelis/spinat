import pandas as pd
import numpy as np
from abc import ABC, abstractmethod


class AbstractProcess(ABC):
    def __init__(self):
        self.fig_time_interval = 120
        self.fig_style = "seaborn-deep"
        self.line_width = 2.0
        self.fig_size = (10, 8)
        self.fig_scatter = True
        self.edge_color = "red"
        self.edge_line_width = 2.5

    def read_expr(self, file, col_names, skip_row, sep):
        lines = open(file, "r").readlines()
        lines = lines[skip_row:]

        parsed_lines = []
        for i, line in enumerate(lines):
            line = line.strip().split(sep)
            line = filter(lambda val: val != "", line)
            line = list(map(float, line))
            parsed_lines.append(line)

        arr = np.array(parsed_lines)
        df = pd.DataFrame(arr[:, :len(col_names)], columns=col_names)

        return df

    @abstractmethod
    def preprocess(self, file_path):
        return NotImplementedError

    @abstractmethod
    def analyze(self, df):
        return NotImplementedError
