from src import preprocess
import seaborn as sb
from matplotlib import pyplot as plt

MOKE_COL_NAMES = ["Field", "Kerr"]


def data_preprocess(file):
    df = preprocess.read_expr(file, MOKE_COL_NAMES)
    df = cleanup0field(df)
    df = join_head2tail(df)
    df = adjust_position(df)

    return df


def cleanup0field(df):
    zero_index = df[df["Field"] == 0].index
    zero_index = zero_index[1::2]
    df = df.drop(zero_index)
    df = df.reset_index(drop=True)

    return df


def join_head2tail(df):
    row = df.loc[df.shape[0]-1, :]
    df = df.append(row)
    df = df.reset_index(drop=True)

    return df


def adjust_position(df):
    center = df[df["Field"] == 0].mean()[1]
    df["Kerr"] = df["Kerr"] - center

    return df


def plot_moke(df, label="", p=None):
    if p is None:
        sb.set()
        p = plt.subplots()

    p[1].plot(
        df["Field"], df["Kerr"],
        label=label, linewidth=2.0)
    p[1].set_xlabel("Field (Oe)")
    p[1].set_ylabel("Kerr Intensity (arb. unit)")
    p[1].legend()
    p[1].grid(True)
    p[1].set_title("MOKE")

    return p
