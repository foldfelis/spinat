from spinat import moke


def main():
    file = "./Demo/MOKE/3FeCu_z62_P_200Oe.txt"
    df = moke.data_preprocess(file)
    print(df)
    p = moke.plot_moke(df, "3 ML Fe/Cu(001)")
    p[0].show()
    p = moke.plot_moke(df, "3 ML Fe/Cu(001)", p)
    p[0].show()


if __name__ == '__main__':
    main()
