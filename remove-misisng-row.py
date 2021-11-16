'''
4. Xóa các dòng bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trước (Ví dụ: xóa các dòng bị
thiếu hơn 50% giá trị các thuộc tính).
'''
import pandas as pd
import argparse

# create a ArgumentParser object.
parser = argparse.ArgumentParser(description="remove all rows that have ratio of missing values \
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

# read file .csv
df = pd.read_csv(infile)

# create a dict from dataframe
new_df = dict(df)

for r in range(len(df)):
    ratio = 0
    for c in new_df.keys():
        if pd.isna(new_df[c][r]):
            ratio = ratio + 1
            
    n = len(new_df.keys())
    if (ratio/n) > (threshold/100):
        for col in new_df.keys():
            del new_df[col][r]
        break

# export new dict to a .csv file by user specified.
with open(outfile, 'w') as f:
    f.write(','.join(new_df.keys()) + '\n')
    
    for i in range(len(df[list(new_df.keys())[0]])):
        line = []
        for k in new_df.keys():
            line.append(str(new_df[k][i]))
            
        f.write(','.join(line) + '\n')
