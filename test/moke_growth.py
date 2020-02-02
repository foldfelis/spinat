from spinat import moke_growth


def moke_growth_1mode_file_test():
    file = "./Demo/MOKE_Growth/14NiCu.bin"
    iop = "o"
    df = moke_growth.data_preprocess(file, False, iop)
    print(df)
    p = moke_growth.plot_moke_growth(df, "MR", iop, "14 ML Ni/Cu(001) MR")
    p = moke_growth.plot_moke_growth(df, "MS", iop, "14 ML Ni/Cu(001) MS", p=p)
    p.show()


def moke_growth_2mode_file_test():
    file = "./Demo/MOKE_Growth/4FeCu.bin"
    df = moke_growth.data_preprocess(file, True)
    print(df)
    p = moke_growth.plot_moke_growth(df, "MR", "i", "4 ML Fe/Cu(001) in-plane MR")
    p = moke_growth.plot_moke_growth(df, "MS", "i", "4 ML Fe/Cu(001) in-plane MS", p=p)
    p = moke_growth.plot_moke_growth(df, "MR", "o", "4 ML Fe/Cu(001) out-of-plane MR", p=p)
    p = moke_growth.plot_moke_growth(df, "MS", "o", "4 ML Fe/Cu(001) out-of-plane MS", p=p)
    p.show()


def main():
    moke_growth_1mode_file_test()
    moke_growth_2mode_file_test()


if __name__ == '__main__':
    main()
