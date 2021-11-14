'''
3. Điền giá trị bị thiếu bằng phương pháp mean, median (cho thuộc tính numeric) và mode
(cho thuộc tính categorical). Lưu ý: khi tính mean, median hay mode các bạn bỏ qua giá
trị bị thiếu.
'''
from numpy import ceil
import pandas as pd
import argparse


# initialize one ArgumemtnParser object to parse argument in command line.
parser = argparse.ArgumentParser(description="Fill all missing value in a specified column use mean, median, mode method")

# add argument parser for input file name.
parser.add_argument('infile',type=str, help="input file's name")

# add argument parser for method.
parser.add_argument('-m', '--method', type=str, metavar='', help="method to filling missing value mean,median for numeric and mode for categorical")

# add argument parser for column.
parser.add_argument('-c', '--columns',required=True, metavar='', type=str, nargs='+', help="name of column")

# add argument parser for output file name.
parser.add_argument('-o', '--out', required=True, metavar='', type=str, help="name of output file")

# get all arguments that user input in command line.
args = parser.parse_args()

# get argument from each argument parser.
method = args.method
outfile = args.out
columns = args.columns
infile = args.infile


# read file .csv
df = pd.read_csv(infile)

# if user doesn't specify method.
if method is None:
    num_cols = []
    cat_cols = []
    for col in columns:
        if df[col].dtypes in ['int64', 'float64']:
            num_cols.append(col)
        else:
            cat_cols.append(col)
    
    # set default method for numeric data is mean
    if len(num_cols) != 0:
        for col in num_cols:
            temp = list(df[col])
            temp = [i for i in temp if pd.isna(i) != True]

            fill_val = sum(temp)/len(temp)

            for i, v in enumerate(df[col]):
                if pd.isna(v):
                    df.loc[i, col] = fill_val
    
    # set default method for categorical data is
    if len(cat_cols) != 0:
        for col in cat_cols:
            temp = list(df[col])
            temp = [i for i in temp if pd.isna(i) != True]

            d  = dict()

            for i in set(temp):
                d[i] = temp.count(i)

            fill_val = max(d)

            for i, v in enumerate(df[col]):
                if pd.isna(v):
                    df.loc[i, col] = fill_val
    
    # if user specify a method
    else:
        for col in columns:
            temp = list(df[col])
            temp = [i for i in temp if pd.isna(i) != True]
            fill_val = None

            # calculate value which is used to fill for missing value in a column.
            if method == "mean":
                fill_val = sum(temp)/len(temp)
            elif method == "median":
                ind_median = ceil(len(temp)/2)
                fill_val = temp[ind_median]
            elif method == "mode":
                d  = dict()

                for i in set(temp):
                    d[i] = temp.count(i)

                fill_val = max(d)

            for i, v in enumerate(df[col]):
                if pd.isna(v):
                    df.loc[i, col] = fill_val

# export to specified a output file's name.
d = dict(df)

with open(outfile, 'w') as f:
    f.write(','.join(d.keys()) + '\n')
    
    for i in range(len(df[columns[0]])):
        line = []
        for k in d.keys():
            line.append(str(d[k][i]))
        
        f.write(','.join(line) + '\n')
