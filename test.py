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


# initialize one ArgumemtnParser object to parse argument in command line.
parser = argparse.ArgumentParser(description="Create a new attribute from multiple attributes.")

# add argument parser for input file name.
# parser.add_argument('infile',type=str, help="input file's name")

# add argument parser for method.
parser.add_argument('--operations', required=True, type=str, metavar='', nargs='+', help="operations (+,-,*,/) use to create a formula\
                                                                                e.g:--operations + - ")

# add argument parser for column.
parser.add_argument('-c', '--columns',required=True, metavar='', type=str, nargs='+', help="name of columns")

# add argument parser for output file name.
# parser.add_argument('-o', '--out', required=True, metavar='', type=str, help="name of output file")

# get all arguments that user input in command line.
args = parser.parse_args()

# get argument from each argument parser.
operations = args.operations
# outfile = args.out
columns = args.columns
# infile = args.infile

if len(columns) != len(operations) + 1:
    sys.exit("Number of columns and number of operations doesn's consistent!!")

# read file .csv
# df = pd.read_csv(infile)

    



# for i in len(df):
    # temp = 0
    
