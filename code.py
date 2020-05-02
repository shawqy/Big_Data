import pandas as pd
import numpy as np
import itertools as itr
import pprint

''' 
read_data_from_txt function 
input : file_path 
        sep_by ==> how the data is separated in the txt file
return : the data frame which we will work on
'''


def read_data_from_txt(file_path='data_set.txt', sep_by='\t'):
    df = pd.read_csv(file_path, delimiter=sep_by)
    return df


''' 
select_col function 
input : data_frame
        col_name ==> column name which we want to separate
return : array containing the data of column
'''


def select_col(data_frame, col_name):
    col_data = []
    for temp in data_frame[col_name]:
        col_data.append(temp)
    return col_data


''' 
get_unique_without_zero function 
input :array
return : array containing the data unique element without zero
'''


def get_unique_without_zero(array):
    col_unique = list(dict.fromkeys(array))
    if col_unique.count(0) > 0:
        col_unique.remove(0)
    return col_unique


# testing function
our_data_frame = read_data_from_txt()
print(our_data_frame)
print((our_data_frame.head(0)))

col = select_col(our_data_frame, 'MBERARBG Skilled labourers')
print(col)
col_u = get_unique_without_zero(col)
print(col_u)

