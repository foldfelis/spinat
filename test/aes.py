from spinat import aes


def main():
    file = "./Demo/AES/14NiCu.agt"
    df = aes.data_preprocess(file)
    print(df)

    p = aes.plot_aes(df, "14 Ni/Cu(001)")
    p.show()

    edge920 = aes.find_edge(df, energy=920, tolerance=6)
    edge783 = aes.find_edge(df, energy=783, tolerance=20)
    for point in edge920:
        print(point, "\n")
    for point in edge783:
        print(point, "\n")

    p = aes.plot_edge(edge920, p, "920")
    p = aes.plot_edge(edge783, p, "783")
    p.show()

    ratio = aes.calc_edge_ratio_on(edge783, edge920)
    p.gca().set_title("AES Cu920/Ni783={}".format(ratio))
    p.show()


if __name__ == '__main__':
    main()
