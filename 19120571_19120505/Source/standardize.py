'''
7. Chuẩn hóa một thuộc tính numeric bằng phương pháp min-max và Z-score.
'''
from math import sqrt
import pandas as pd
import argparse
import sys
import re


def mean(col):
    '''calculate mean of one column
    
    Parameters
    -----------
        col (...): 1 column in a dataframe.
    
    Returns
    ----------
        mean (double): mean of one column.
    '''
    c = [i for i in col if pd.isna(i) == False]
    m = sum(c) / len(col)
    return m

def std(col):
    '''calculate standard deviation of 1 column in a dataframe.
    
    Parameters
    ----------
        col: 1 column in a dataframe.

    Returns
    ---------
        std (doublel): std of one column.
    '''
    c = [i for i in col if pd.isna(i) == False]
    m = mean(col)
    n = len(c) - 1
    s = 0

    for i in c:
        s = s + (i - m)**2

    return sqrt(s/n)



# create a ArgumentParser object.
parser = argparse.ArgumentParser(description="Standardize numeric attributes use min-max method and Z-score")

# add an argument parser for input file's name.
parser.add_argument('infile', help="name of input file")

# add an argument parser for method.
parser.add_argument('-m', '--method', metavar='', help="standardize method min-max and z-score")

# add an argument parser for column.
parser.add_argument('-c', '--column', required=True, metavar='', help="name of 1 numeric column in dataframe")

# add an argument parser for output file's name.
parser.add_argument('-o', '--out', required=True, metavar='', help="output file's name")

# get all arguments have been passed to command line by user.
args = parser.parse_args()

# assign each argument to a variable.
infile = args.infile
method = args.method
column = args.column
outfile = args.out

# read csv file
df = pd.read_csv(infile)

# check if input column is a numeric otherwise exit.
if df[column].dtypes == 'object':
    sys.exit('Error, input column is not a numeric column')
else:
    pass

if method:
    # standardize method string
    method = ' '.join(w for w in re.split(r"\W", method) if w)
    method = method.lower()
else:
    method = 'min max'


if method == 'min max':
    min_val = min(df[column])
    max_val = max(df[column])
    for i in range(len(df[column])):
        df.loc[i, column] = (df.loc[i, column] - min_val)/(max_val - min_val)
elif method == 'z score':
    mean_val = mean(df[column])
    std_val = std(df[column])

    for i in range(len(df[column])):
        df.loc[i, column] = (df.loc[i, column] - mean_val)/std_val

# make a new dict from a dataframe.
df.to_csv(outfile, index=False)
