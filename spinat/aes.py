import pandas as pd
from matplotlib import pyplot as plt
from spinat.process import AbstractProcess

AES_COL_NAMES = ["ElectronEnergy", "dNdE"]


class AesProcess(AbstractProcess):
    def __init__(self, header_rows=34, encoding="latin1", sep="\t"):
        super().__init__()
        self._col_names = AES_COL_NAMES
        self._header_rows = header_rows
        self._encoding = encoding
        self._sep = sep
        self.low_thickness_sensitive = True
        self.based_energy = 920
        self.based_tol = 5
        self.element_energy = 717
        self.element_tol = 5
        self.fig_size = (20, 7)
        self.fig_scatter = False

    def read_expr(self, file, col_names, skip_row, sep):
        df = pd.read_csv(
            file, names=col_names,
            skiprows=skip_row, sep=sep
        )

        return df

    @classmethod
    def parse_argv(cls, file_path, header_rows, encoding, sep):
        args = {}
        with open(file_path, "r", encoding=encoding) as f:
            for i, line in enumerate(f.readlines()):
                if i == header_rows - 1:
                    break
                if line.startswith("{") \
                        or line.startswith("}") \
                        or line.startswith("["):
                    continue
                tokens = line.replace(sep, " ").strip().split(" ", 1)
                if len(tokens) < 2:
                    tokens.append("")
                args[tokens[0]] = tokens[1]

        return args

    @classmethod
    def reset_energy(cls, df, argv):
        step_interval = float(argv["StepInterval"])
        star_energy = float(argv["StartEnergy"])
        df["ElectronEnergy"] = df["ElectronEnergy"] * step_interval + star_energy

        return df

    def preprocess(self, file_path):
        args = self.parse_argv(file_path, self._header_rows, self._encoding, self._sep)
        df = self.read_expr(file_path, self._col_names, self._header_rows, self._sep)
        df = self.reset_energy(df, args)

        return df

    @classmethod
    def find_edge(cls, df, energy, tolerance):
        edge_df = df[df["ElectronEnergy"].between(
            energy - tolerance, energy + tolerance)]

        edge = [
            df.iloc[edge_df["dNdE"].idxmax()],
            df.iloc[edge_df["dNdE"].idxmin()]
        ]

        return edge

    @classmethod
    def calc_edge_ratio_on(cls, element_edge, based_edge, low_thickness_sensitive):
        based_delta_dnde = based_edge[0]["dNdE"] - based_edge[1]["dNdE"]
        element_delta_dnde = element_edge[0]["dNdE"] - element_edge[1]["dNdE"]

        if low_thickness_sensitive:
            ratio = based_delta_dnde / element_delta_dnde
        else:
            ratio = element_delta_dnde / based_delta_dnde

        return ratio

    def analyze(self, df):
        based_edge = self.find_edge(df, self.based_energy, self.based_tol)
        element_edge = self.find_edge(df, self.element_energy, self.element_tol)
        ratio = self.calc_edge_ratio_on(element_edge, based_edge, self.low_thickness_sensitive)

        data = {
            "based_edge": based_edge,
            "element_edge": element_edge,
            "ratio": ratio,
        }

        return data

    def plot(self, df, label="", p=None):
        with plt.style.context(self.fig_style):
            if p is None:
                p = plt.figure(figsize=self.fig_size)

            energy = df["ElectronEnergy"]
            dn_de = df["dNdE"]

            ax = p.gca()
            if self.fig_scatter:
                ax.scatter(energy, dn_de, label=label)
            else:
                ax.plot(
                    energy, dn_de,
                    label=label, linewidth=self.line_width)

            ax.set_xlabel("ElectronEnergy (eV)")
            ax.set_ylabel("dN/dE")
            ax.legend()
            ax.grid(True)
            ax.set_title("AES")

        return p

    def plot_edge(self, edge, p, label=""):
        delta_energy = []
        delta_dnde = []
        for point in edge:
            delta_energy.append(point.ElectronEnergy)
            delta_dnde.append(point.dNdE)

        ax = p.gca()
        ax.plot(
            delta_energy, delta_dnde, color=self.edge_color,
            label=label, linewidth=self.edge_line_width)
        ax.legend()

        return p
