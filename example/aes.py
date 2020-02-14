from os.path import join as join_path
from os import listdir

from spinat import aes


def main():
    """
        Deposit Cu on 14 ML Ni/Cu(001)
    """

    data_path = "../DemoData/AES"
    ap = aes.AesProcess()
    ap.low_thickness_sensitive = True
    ap.based_energy = 717
    ap.based_tol = 16
    ap.element_energy = 920
    ap.element_tol = 6

    files = listdir(data_path)
    files.sort()
    p = None
    for file in files:
        df = ap.preprocess(join_path(data_path, file))
        data = ap.analyze(df)
        p = ap.plot(df, label="{}, ratio={}".format(file, data["ratio"]), p=p)
        p = ap.plot_edge(edge=data["based_edge"], p=p, label="{}".format(ap.based_energy))
        p = ap.plot_edge(edge=data["element_edge"], p=p, label="{}".format(ap.element_energy))

    p.show()


if __name__ == '__main__':
    main()
