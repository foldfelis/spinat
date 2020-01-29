from spinat import preprocess

COL_NAMES_MOKE_GROWTH_2MODE = [
        "Time_i", "FluxSum1_i", "FluxSum2_i",
        "MR_i", "MS_i", "MaxField_i",
        "Logic_i", "Temp_i", "Pressure_i",

        "Time_o", "FluxSum1_o", "FluxSum2_o",
        "MR_o", "MS_o", "MaxField_o",
        "Logic_o", "Temp_o", "Pressure_o",
]

COL_NAMES_MOKE = ["Field", "Kerr"]


def moke_growth_2mode_file_test():
    file = "./Demo/MOKE_Growth/4FeCu.bin"
    df = preprocess.read_expr(file, COL_NAMES_MOKE_GROWTH_2MODE, skip_row=2, sep=" ")

    return df


def moke_growth_partial_2mode_file_test():
    file = "./Demo/MOKE_Growth/4FeCu.bin"
    col = COL_NAMES_MOKE_GROWTH_2MODE[:int(len(COL_NAMES_MOKE_GROWTH_2MODE) / 2)]
    df = preprocess.read_expr(file, col, skip_row=2, sep=" ")

    return df


def moke_growth_1mode_file_test():
    file = "./Demo/MOKE_Growth/14NiCu.bin"
    iop = "o"
    col_names = [
        f"Time_{iop}",
        f"Flux1_{iop}", f"Flux2_{iop}",
        f"FluxSum1_{iop}", f"FluxSum2_{iop}",
        f"MR_{iop}", f"MS_{iop}",
        f"DC_MR_{iop}", f"DC_MS_{iop}",
        f"MaxField_{iop}", f"Logic_{iop}",
        f"Temp_{iop}", f"Pressure_{iop}",
    ]
    df = preprocess.read_expr(file, col_names, skip_row=2, sep=" ")

    return df


def moke_ncue_file_test():
    file = "./Demo/MOKE/3FeCu_z62_P_200Oe.txt"
    df = preprocess.read_expr(file, COL_NAMES_MOKE, skip_row=0, sep=" ")

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


if __name__ == '__main__':
    main()
