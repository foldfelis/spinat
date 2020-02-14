from os.path import join as join_path
from os import listdir

from spinat import moke


def main():
    data_path = "../DemoData/MOKE"
    mp = moke.MokeProcess()

    files = listdir(data_path)
    files.sort()
    p = None
    for file in files:
        df = mp.preprocess(join_path(data_path, file))
        p = mp.plot(df, label=file, p=p)

    p.show()


if __name__ == '__main__':
    main()
