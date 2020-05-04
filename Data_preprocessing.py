import pandas as pd
import numpy as np

''' 
read_data_from_txt function 
input : file_path 
        sep_by ==> how the data is separated in the txt file
return : numpy 2D array containing the data
'''


def read_data_from_txt(file_path='ticdata2000.txt', sep_by='\t'):
    df = pd.read_csv(file_path, delimiter=sep_by)

    return df.to_numpy()


''' 
split_data_with_index function 
input : full_data_2D_array
        selected_index ==> start index for getting the data
return : numpy 2D array containing the data
'''


def split_data_with_index(full_data_2D_array, selected_index=23):
    # selected_index -=1 as 2D array start from index 0 not 1
    selected_index = selected_index - 1
    return full_data_2D_array[:, selected_index: selected_index + 12]


''' 
append_col_index function 
input : input_data
return : numpy 2D array containing the data values with column index
'''


def append_col_index(input_data):
    # empty array for result
    data_unique_per_col = np.empty(input_data.shape, dtype=np.dtype('U100'))

    # append column index to each value
    for col_id in range(input_data.shape[1]):
        for row_id in range(input_data.shape[0]):
            data_unique_per_col[row_id][col_id] = str(int(input_data[row_id][col_id])) + '_' + str(col_id)
    return data_unique_per_col


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

