from spinat import datafiles


def moke_growth_2mode_file_test():
    fn = "/home/n/GoogleDrive/Lab/Data/Demo/MOKE_Growth/4FeCu.bin"
    col_names = [
        "Time_i", "FluxSum1_i", "FluxSum2_i",
        "MR_i", "MS_i", "MaxField_i",
        "Logic_i", "Temp_i", "Pressure_i",

        "Time_o", "FluxSum1_o", "FluxSum2_o",
        "MR_o", "MS_o", "MaxField_o",
        "Logic_o", "Temp_o", "Pressure_o",
    ]
    df = datafiles.file2df(fn, col_names, n_header=2, sep=" ")

    return df


def moke_growth_partial_2mode_file_test():
    fn = "/home/n/GoogleDrive/Lab/Data/Demo/MOKE_Growth/4FeCu.bin"
    col_names = [
        "Time_i", "FluxSum1_i", "FluxSum2_i",
        "MR_i", "MS_i", "MaxField_i",
        "Logic_i", "Temp_i", "Pressure_i",
    ]
    df = datafiles.file2df(fn, col_names, n_header=2, sep=" ")

    return df


def moke_growth_1mode_file_test():
    fn = "/home/n/GoogleDrive/Lab/Data/Demo/MOKE_Growth/14NiCu.bin"
    iop = "o"
    col_names = [
        f"Time_{iop}",
        f"Flux1_{iop}", f"Flux2_{iop}",
        f"FluxSum1_{iop}", f"FluxSum2_{iop}",
        f"MR_{iop}", f"MS_{iop}", f"DC_MR_{iop}", f"DC_MS_{iop}",
        f"MaxField_{iop}", f"Logic_{iop}", f"Temp_{iop}", f"Pressure_{iop}",
    ]
    df = datafiles.file2df(fn, col_names, n_header=2, sep=" ")

    return df


def main():
    df = moke_growth_2mode_file_test()
    print(df)

    df = moke_growth_partial_2mode_file_test()
    print(df)

    df = moke_growth_1mode_file_test()
    print(df)


if __name__ == '__main__':
    main()
