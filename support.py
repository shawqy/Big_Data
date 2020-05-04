import itertools as itr
import support as s
import globals_values as g


''' 
data_set_support function 
input : data_col ==> data after being related to each column 
        support ==> min. support
        previous_item_sets ==> previous levels support
return :dictionary containing support for the data set
'''


def data_set_support(data_col, support, previous_item_sets=[], support_lvl=1):
    if support_lvl == 1:
        # to append values and its counts
        item_sets_count = {}

        for col_id in range(data_col.shape[1]):
            for rw_id in range(data_col.shape[0]):
                val = data_col[rw_id][col_id]
                # if the value is 0 skip it
                if val.find('0_') == 0:
                    continue
                if val in item_sets_count.keys():
                    item_sets_count[val] += 1
                else:
                    item_sets_count[val] = 1

    elif support_lvl > 1:
        item_sets_count = {}
        for itemset in list(itr.combinations(previous_item_sets, support_lvl)):
            key = ','.join(itemset)
            item_sets_count[key] = 0
            items_exist_together = True

            for row in data_col:
                for item in itemset:
                    if not item in row:
                        items_exist_together = False
                        break
                if items_exist_together:
                    item_sets_count[key] += 1

                items_exist_together = True

    # find items under Min. support
    items_under_support = []
    for itemset in item_sets_count.keys():
        if float(item_sets_count[itemset]) / data_col.shape[0] < support:
            items_under_support.append(itemset)

    # remove items under Min. support
    for itemset in items_under_support:
        del item_sets_count[itemset]

    if len(item_sets_count.keys()) == 0:
        # DONE
        return

    else:
        support_lvl += 1
        itemsets = []
        for item in item_sets_count.keys():
            itemsets += list(set(item.split(',')) - set(itemsets))

        s.data_set_support(data_col, support, itemsets, support_lvl)
        g.final_item_counts.update(item_sets_count)

