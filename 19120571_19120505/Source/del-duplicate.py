'''
6. Xóa các mẫu bị trùng lặp.
'''
import pandas as pd
import argparse

# create a ArgumentParser object.
parser = argparse.ArgumentParser(description="Delete duplicate instance in a dataset")

# add an argument parser for input file's name.
parser.add_argument('infile', help="name of input file")

# add an argument parser for output file's name.
parser.add_argument('-o', '--out', required=True, metavar='', help="output file's name")

# get all arguments have been passed to command line by user.
args = parser.parse_args()

infile = args.infile
outfile = args.out

# read .csv file
df = pd.read_csv(infile)

# create a dict from dataframe
new_df = dict(df)

for r in range(len(new_df[list(new_df.keys())[0]])):
    flag = True
    for row in range(r + 1, len(new_df[list(new_df.keys())[0]])):
        for c in new_df.keys():
            if list(new_df[c])[row] != list(new_df[c])[r] and pd.isna(list(new_df[c])[r]) == False\
                and pd.isna(list(new_df[c])[row]) == False:
                flag = False
                break
        
        if flag:
            for col in new_df.keys():
                del list(new_df[col])[row]

# export new dict to a .csv file by user specified.
pd.DataFrame(new_df).to_csv(outfile, index=False)
