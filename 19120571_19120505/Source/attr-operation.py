'''
8. Tính giá trị biểu thức thuộc tính: ví dụ đối với một tập dữ liệu có chứa 2 thuộc tính width
và height thì biểu thức width ∗ height sẽ trả về tập dữ liệu cũ với một thuộc tính mới có
giá trị ở mỗi mẫu là tích của thuộc tính width và height trong mẫu tương ứng, với điều
kiện cả 2 giá trị width và height đều không bị thiếu, trong trường hợp bị thiếu thì giá trị
biểu thức coi như bị thiếu. Lưu ý: biểu thức có thể có nhiều thuộc tính và nhiều phép toán
bao gồm cộng, trừ, nhân, chia.
'''
import sys
import pandas as pd
import argparse
import re
import numpy as np

# initialize one ArgumemtnParser object to parse argument in command line.
parser = argparse.ArgumentParser(description="Create a new attribute from multiple attributes.")

# add argument parser for input file name.
parser.add_argument('infile',type=str, help="input file's name")

# add argument parser for new column's name.
parser.add_argument('-n', '--cname',type=str, metavar='', help="new column's name")

# add argument parser for operations.
parser.add_argument('--operations', required=True, type=str, metavar='', nargs='+', help="operations (+,-,*,/) use to create a formula\
                                                                                e.g:--operations + - ")

# add argument parser for column.
parser.add_argument('-c', '--columns',required=True, metavar='', type=str, nargs='+', help="name of columns")

# add argument parser for output file name.
parser.add_argument('-o', '--out', required=True, metavar='', type=str, help="name of output file")

# get all arguments that user input in command line.
args = parser.parse_args()

# get argument from each argument parser.
operations = args.operations
outfile = args.out
columns = args.columns
infile = args.infile
cname = args.cname

# if user doesn't specify a name for new column
# set it to default name "new_column"
if cname is None:
    cname = 'new_column'
else:
    # standardize cname string
    cname = '_'.join(w for w in re.split(r"\W", cname) if w)

# 
if len(columns) != len(operations) + 1:
    sys.exit("Number of columns and number of operations doesn's consistent!!")

# read file .csv
df = pd.read_csv(infile)

# create a list for storing values to make a new column.
new_col = []

# calculate value for new column.
for i in range(len(df)):
    val = df.loc[i, columns[0]]
    for c, j in zip(columns[1:], operations):
        if pd.isna(df.loc[i, c]):
            val = np.nan
            break
        if j == '+':
            val = val + df.loc[i, c]
        elif j == '-':
            val = val - df.loc[i, c]
        elif j == '*':
            val = val * df.loc[i, c]
        elif j == '/':
            val = val / df.loc[i, c]
    
    # append value correspond to each row.
    new_col.append(val)

# add new column with a new name specified by user.
df[cname] = new_col

# export to .csv file.
df.to_csv(outfile, index=False)
