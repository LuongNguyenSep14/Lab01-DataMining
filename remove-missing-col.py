'''
5. Xóa các cột bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trước (Ví dụ: xóa các cột bị thiếu
giá trị thuộc tính ở hơn 50% số mẫu).
'''
import pandas as pd
import argparse

# create a ArgumentParser object.
parser = argparse.ArgumentParser(description="remove all columns that have ratio of missing values \
                                                greater than a specified threshold")

# add an argument parser for input file's name.
parser.add_argument('infile', help="name of input file")

# add an argument parser for threshold.
parser.add_argument('-t', '--threshold', metavar='', help="threshold")

# add an argument parser for output file's name.
parser.add_argument('-o', '--out', required=True, metavar='', help="output file's name")

# get all arguments have been passed to command line by user.
args = parser.parse_args()

# assign each argument to a variable.
infile = args.infile
threshold = args.threshold
outfile = args.out

# set default value of threshold to 50% if user doesn't specify.
if threshold is None:
    threshold = 50

# init a list to store name of column that have
# missing value.
cols_with_missing = []


# read file .csv
df = pd.read_csv(infile)

# find all columns that have missing values.
for col in df.columns:
    # check if that col have missing value.
    if df[col].isna().any():
        cols_with_missing.append(col)


# make a new dict from a dataframe.
new_df = dict(df)


# remove all columns that have a ratio of missing value greater than
# a specified threshold.
for col in cols_with_missing:
    # number of missing values in a column.
    num_missing = len([m for m in df[col] if pd.isna(m)])
    # ratio of missing values over all values in a column.
    ratio_of_missing = num_missing / len(df[col])

    if ratio_of_missing < 50/100:
        del new_df[col]


# export new dict to a .csv file by user specified.
with open(outfile, 'w') as f:
    f.write(','.join(new_df.keys()) + '\n')
    
    for i in range(len(df[list(new_df.keys())[0]])):
        line = []
        for k in new_df.keys():
            line.append(str(new_df[k][i]))
            
        f.write(','.join(line) + '\n')
