from matplotlib import pyplot as plt
from spinat.process import AbstractProcess

MOKE_GROWTH_MULTI_MODE_COL_NAMES = [
    "Time_i", "FluxSum1_i", "FluxSum2_i",
    "MR_i", "MS_i", "MaxField_i",
    "Logic_i", "Temp_i", "Pressure_i",

    "Time_o", "FluxSum1_o", "FluxSum2_o",
    "MR_o", "MS_o", "MaxField_o",
    "Logic_o", "Temp_o", "Pressure_o",
]


class MokeGrowthProcess(AbstractProcess):
    def __init__(self, multi_mode=True, iop="i", skip_row=2, sep=" "):
        super().__init__()
        self.col_names = MOKE_GROWTH_MULTI_MODE_COL_NAMES
        self._multi_mode = multi_mode
        self._iop = iop
        self._skip_row = skip_row
        self._sep = sep
        self.prepare_time = 60

    def get_column_names(self):
        return self.col_names

    def set_column_names(self, multi_mode, iop):
        if not multi_mode:
            self.col_names = [
                f"Time_{iop}",
                f"Flux1_{iop}", f"Flux2_{iop}",
                f"FluxSum1_{iop}", f"FluxSum2_{iop}",
                f"MR_{iop}", f"MS_{iop}",
                f"DC_MR_{iop}", f"DC_MS_{iop}",
                f"MaxField_{iop}", f"Logic_{iop}",
                f"Temp_{iop}", f"Pressure_{iop}",
            ]
        else:
            self.col_names = MOKE_GROWTH_MULTI_MODE_COL_NAMES

    @classmethod
    def adjust_time(cls, df, multi_mode, iop, prepare_time):
        if multi_mode:
            df["Time_i"] = df["Time_i"] - prepare_time
            df["Time_o"] = df["Time_o"] - prepare_time
        else:
            df[f"Time_{iop}"] = df[f"Time_{iop}"] - prepare_time

        return df

    def preprocess(self, file_path):
        self.set_column_names(self._multi_mode, self._iop)
        df = self.read_expr(file_path, self.col_names, self._skip_row, self._sep)
        df = self.adjust_time(df, self._multi_mode, self._iop, self.prepare_time)

        return df

    def analyze(self, df):
        pass

    def plot(self, df, mr_ms, iop, label="", p=None):
        if mr_ms == "MR":
            kerr_col_name = f"MR_{iop}"
        elif mr_ms == "MS":
            kerr_col_name = f"MS_{iop}"
        else:
            print("argument 'mr_ms' is ether 'MR' or 'MS'")
            return p

        with plt.style.context(self.fig_style):
            if p is None:
                p = plt.figure(figsize=self.fig_size)

        time = df[f"Time_{iop}"].values
        kerr = df[kerr_col_name].values

        ax = p.gca()
        if self.fig_scatter:
            ax.scatter(time, kerr, label=label)
        else:
            ax.plot(
                time, kerr,
                label=label, linewidth=self.line_width)

        ax.set_xlabel("Time (sec)")
        ax.set_ylabel("Kerr Intensity (arb. unit)")
        ax.set_xticks(range(-self.prepare_time, int(max(time)), self.fig_time_interval))
        ax.legend()
        ax.grid(True)
        ax.set_title("MOKE Growth")

        return p
