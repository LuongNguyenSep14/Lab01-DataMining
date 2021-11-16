'''
2. Đếm số dòng bị thiếu dữ liệu.
'''
import pandas as pd
import argparse

# create a ArgumentParser object.
parser = argparse.ArgumentParser(description="Count number of row that have missing value")

# add an argument parser for input file's name.
parser.add_argument('infile', help="name of input file")

# get all arguments have been passed to command line by user.
args = parser.parse_args()

infile = args.infile

# read .csv file
df = pd.read_csv(infile)

# initialize var to store number of row that have missing value.
num_missing_row = 0

# loop through all rows of dataframe to count all rows that have
# missing value.
for r in range(len(df)):
    for c in df.columns:
        if pd.isna(df.loc[r, c]):
            num_missing_row = num_missing_row + 1
            break

# print out number of rows.
print('Number of rows that have missing value: %d' % (num_missing_row))
