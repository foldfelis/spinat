from spinat import datafiles


def main():
    fn = "/home/n/GoogleDrive/Lab/Data/Demo/MOKE_Growth/4FeCu.bin"
    lines = datafiles.file2lines(fn)
    lines = datafiles.remove_header(lines, 2)
    arr = datafiles.lines2array(lines, sep=" ")
    col_names = [
        "Time_i", "FluxSum1_i", "FluxSum2_i",
        "MR_i", "MS_i", "MaxField_i",
        "Logic_i", "Temp_i", "Pressure_i",

        "Time_o", "FluxSum1_o", "FluxSum2_o",
        "MR_o", "MS_o", "MaxField_o",
        "Logic_o", "Temp_o", "Pressure_o",
    ]
    df = datafiles.array2df(arr, col_names)
    print(df)


if __name__ == '__main__':
    main()
