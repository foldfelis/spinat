from spinat import datafiles


def moke_growth_2mode_file_test():
    fn = "./Demo/MOKE_Growth/4FeCu.bin"
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
    fn = "./Demo/MOKE_Growth/4FeCu.bin"
    col_names = [
        "Time_i", "FluxSum1_i", "FluxSum2_i",
        "MR_i", "MS_i", "MaxField_i",
        "Logic_i", "Temp_i", "Pressure_i",
    ]
    df = datafiles.file2df(fn, col_names, n_header=2, sep=" ")

    return df


def moke_growth_1mode_file_test():
    fn = "./Demo/MOKE_Growth/14NiCu.bin"
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


def moke_ncue_file_test():
    fn = "./Demo/MOKE/3FeCu_z62_P_200Oe.txt"
    col_names = ["Field", "Kerr"]
    df = datafiles.file2df(fn, col_names, n_header=0, sep=" ")

    return df


def main():
    df = moke_growth_2mode_file_test()
    print(df)

    df = moke_growth_partial_2mode_file_test()
    print(df)

    df = moke_growth_1mode_file_test()
    print(df)

    df = moke_ncue_file_test()
    print(df)

    """ When read AES file use pandas will do """
    # TODO: Add the following code to AES analysis.
    import pandas as pd
    fn = "./Demo/AES/100-950ev_z63_runs2_NiCu.agt"
    col_names = ["ElectronEnergy", "dNdE"]
    df = pd.read_csv(fn, skiprows=34, sep="\t", names=col_names)
    print(df)
    # TODO: end


if __name__ == '__main__':
    main()
