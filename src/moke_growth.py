from src import preprocess
import seaborn as sb
from matplotlib import pyplot as plt


def data_preprocess(file, multi_mode, iop="i"):
    col_names = set_columns(multi_mode, iop)
    df = preprocess.read_expr(file, col_names, skip_row=2)
    df = adjust_time(df, multi_mode, iop)

    return df


def set_columns(multi_mode, iop):
    if multi_mode:
        col_names = [
            "Time_i", "FluxSum1_i", "FluxSum2_i",
            "MR_i", "MS_i", "MaxField_i",
            "Logic_i", "Temp_i", "Pressure_i",

            "Time_o", "FluxSum1_o", "FluxSum2_o",
            "MR_o", "MS_o", "MaxField_o",
            "Logic_o", "Temp_o", "Pressure_o",
        ]
    else:
        col_names = [
            f"Time_{iop}",
            f"Flux1_{iop}", f"Flux2_{iop}",
            f"FluxSum1_{iop}", f"FluxSum2_{iop}",
            f"MR_{iop}", f"MS_{iop}",
            f"DC_MR_{iop}", f"DC_MS_{iop}",
            f"MaxField_{iop}", f"Logic_{iop}",
            f"Temp_{iop}", f"Pressure_{iop}",
        ]

    return col_names


def adjust_time(df, multi_mode, iop):
    if multi_mode:
        df["Time_i"] = df["Time_i"] - 60
        df["Time_o"] = df["Time_o"] - 60
    else:
        df[f"Time_{iop}"] = df[f"Time_{iop}"] - 60

    return df


def plot_moke_growth(
        df, mr_ms, iop, label="", interval=120,
        style="seaborn-deep", size=(6, 5), p=None, scatter=True):
    if mr_ms == "MR":
        kerr_col_name = f"MR_{iop}"
    elif mr_ms == "MS":
        kerr_col_name = f"MS_{iop}"
    else:
        print("argument 'mr_ms' is ether 'MR' or 'MS'")
        return p

    with plt.style.context(style):
        if p is None:
            p = plt.figure(figsize=size)

    time = df[f"Time_{iop}"].values
    kerr = df[kerr_col_name].values

    ax = p.gca()
    if scatter:
        ax.scatter(time, kerr, label=label)
    else:
        ax.plot(
            time, kerr,
            label=label, linewidth=2.0)

    ax.set_xlabel("Time (sec)")
    ax.set_ylabel("Kerr Intensity (arb. unit)")
    ax.set_xticks(range(-60, int(max(time)), interval))
    ax.legend()
    ax.grid(True)
    ax.set_title("MOKE Growth")

    return p
