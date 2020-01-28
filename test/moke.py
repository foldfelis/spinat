from spinat import moke


def main():
    file = "./Demo/MOKE/3FeCu_z62_P_200Oe.txt"
    df = moke.data_preprocess(file)
    print(df)


if __name__ == '__main__':
    main()
