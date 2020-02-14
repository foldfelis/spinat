from matplotlib import pyplot as plt
from spinat.process import AbstractProcess

MOKE_COL_NAMES = ["Field", "Kerr"]


class MokeProcess(AbstractProcess):
    def __init__(self, skip_row=0, sep=" "):
        super().__init__()
        self._col_names = MOKE_COL_NAMES
        self._skip_row = skip_row
        self._sep = sep

    @classmethod
    def cleanup0field(cls, df):
        zero_index = df[df["Field"] == 0].index
        zero_index = zero_index[1::2]
        df = df.drop(zero_index)
        df = df.reset_index(drop=True)

        return df

    @classmethod
    def join_head2tail(cls, df):
        row = df.loc[df.shape[0] - 1, :]
        df = df.append(row)
        df = df.reset_index(drop=True)

        return df

    @classmethod
    def adjust_position(cls, df):
        center = df[df["Field"] == 0].mean()[1]
        df["Kerr"] = df["Kerr"] - center

        return df

    def preprocess(self, file_path):
        df = self.read_expr(file_path, self._col_names, self._skip_row, self._sep)
        df = self.cleanup0field(df)
        df = self.join_head2tail(df)
        df = self.adjust_position(df)

        return df

    def analyze(self, df):
        pass

    def plot(self, df, label="", p=None):
        with plt.style.context(self.fig_style):
            if p is None:
                p = plt.figure(figsize=self.fig_size)

        ax = p.gca()
        ax.plot(
            df["Field"], df["Kerr"],
            label=label, linewidth=2.0)

        ax.set_xlabel("Field (Oe)")
        ax.set_ylabel("Kerr Intensity (arb. unit)")
        ax.legend()
        ax.grid(True)
        ax.set_title("MOKE")

        return p
