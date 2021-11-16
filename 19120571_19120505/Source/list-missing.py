'''
1. Liệt kê các cột bị thiếu dữ liệu.
'''
import pandas as pd
import argparse

# create a ArgumentParser object.
parser = argparse.ArgumentParser(description="Get name of all columns that have missing values")
# add an argument parser for input file's name.
parser.add_argument('infile', help="name of input file")

# get all arguments have been passed to command line by user.
args = parser.parse_args()

# init a list to store name of column that have
# missing value.
cols_with_missing = []

try:
    # read file .csv
    df = pd.read_csv(args.infile)

    for col in df.columns:
        # check if that col have missing value.
        if df[col].isna().any():
            cols_with_missing.append(col)

except:
    pass

print(cols_with_missing)
