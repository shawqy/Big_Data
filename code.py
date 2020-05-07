# importing helping files
import Data_preprocessing as Dp
import support as s
import globals_values as g
import prepare as p

# taking inputs from user
support = eval(input('Enter Min. Support as fraction "Ex 0.1": '))
confidence = eval(input('Enter Min. confidence as fraction "Ex 0.1": '))
Starting_index = eval(input('Enter The Starting Index: '))
# read the data form the text file
# by default the file is ticdata2000.txt
our_data_frame = Dp.read_data_from_txt()

# printing the read data
print(our_data_frame)

# specify the set of data we want work with
our_data_set = Dp.split_data_with_index(our_data_frame, Starting_index)

# printing this set
print(our_data_set)

# append column index to each value
data = Dp.append_col_index(our_data_set)

# printing the previous result
print(data)

# calculate support
s.data_set_support(data, support)

# print support
finalItems = g.final_item_counts
print(g.final_item_counts)
p.process(finalItems, p.finalSupport(finalItems))
