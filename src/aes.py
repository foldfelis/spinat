import pandas as pd
from matplotlib import pyplot as plt

AES_COL_NAMES = ["ElectronEnergy", "dNdE"]


def parse_argv(file, header_rows):
    args = {}
    with open(file, "r", encoding="latin1") as f:
        for i, line in enumerate(f.readlines()):
            if i == header_rows - 1:
                break
            if line.startswith("{") \
                    or line.startswith("}") \
                    or line.startswith("["):
                continue
            tokens = line.replace("\t", " ").strip().split(" ", 1)
            if len(tokens) < 2:
                tokens.append("")
            args[tokens[0]] = tokens[1]

    return args


def reset_energy(df, argv):
    step_interval = float(argv["StepInterval"])
    star_energy = float(argv["StartEnergy"])
    df["ElectronEnergy"] = df["ElectronEnergy"] * step_interval + star_energy

    return df


def data_preprocess(file):
    header_rows = 34
    args = parse_argv(file, header_rows)
    df = pd.read_csv(
        file, names=AES_COL_NAMES,
        skiprows=header_rows, sep="\t"
    )
    df = reset_energy(df, args)

    return df


def plot_aes(
        df, label="", scatter=False, p=None,
        style="seaborn-deep", size=(10, 5)):
    with plt.style.context(style):
        if p is None:
            p = plt.figure(figsize=size)

        energy = df["ElectronEnergy"]
        dn_de = df["dNdE"]

        ax = p.gca()
        if scatter:
            ax.scatter(energy, dn_de, label=label)
        else:
            ax.plot(
                energy, dn_de,
                label=label, linewidth=2.0)

        ax.set_xlabel("ElectronEnergy (eV)")
        ax.set_ylabel("dN/dE")
        ax.legend()
        ax.grid(True)
        ax.set_title("AES")

    return p


def find_edge(df, energy, tolerance=5):
    edge_df = df[df["ElectronEnergy"].between(
        energy-tolerance, energy+tolerance)]

    edge = [
        df.iloc[edge_df["dNdE"].idxmax()],
        df.iloc[edge_df["dNdE"].idxmin()]
    ]

    return edge


def plot_edge(edge, p, label="", color="red"):
    delta_energy = []
    delta_dnde = []
    for point in edge:
        delta_energy.append(point.ElectronEnergy)
        delta_dnde.append(point.dNdE)

    ax = p.gca()
    ax.plot(
        delta_energy, delta_dnde, color=color,
        label=label, linewidth=2.5)
    ax.legend()

    return p


def calc_edge_ratio_on(element_edge, based_edge, low_thickness_sensitive=True):
    based_delta_dnde = based_edge[0]["dNdE"] - based_edge[1]["dNdE"]
    element_delta_dnde = element_edge[0]["dNdE"] - element_edge[1]["dNdE"]

    if low_thickness_sensitive:
        ratio = based_delta_dnde / element_delta_dnde
    else:
        ratio = element_delta_dnde / based_delta_dnde

    return ratio
