from spinat import moke_growth


def moke_growth_1mode_file():
    file_path = "../DemoData/MOKE_Growth/14NiCu.bin"
    iop = "o"
    mgp = moke_growth.MokeGrowthProcess(multi_mode=False, iop=iop)

    df = mgp.preprocess(file_path)

    p = mgp.plot(df, "MR", iop, "14 ML Ni/Cu(001) MR")
    final_p = mgp.plot(df, "MS", iop, "14 ML Ni/Cu(001) MS", p=p)

    return final_p


def moke_growth_2mode_file():
    file_path = "../DemoData/MOKE_Growth/4FeCu.bin"
    mgp = moke_growth.MokeGrowthProcess()

    df = mgp.preprocess(file_path)

    p = mgp.plot(df, "MR", "i", "4 ML Fe/Cu(001) in-plane MR")
    p = mgp.plot(df, "MS", "i", "4 ML Fe/Cu(001) in-plane MS", p=p)
    p = mgp.plot(df, "MR", "o", "4 ML Fe/Cu(001) out-of-plane MR", p=p)
    final_p = mgp.plot(df, "MS", "o", "4 ML Fe/Cu(001) out-of-plane MS", p=p)

    return final_p


def main():
    moke_growth_1mode_file().show()
    moke_growth_2mode_file().show()


if __name__ == '__main__':
    main()
