import itertools

def getNames(test):

    splitedTest = test.split(',')
    final = []
    for i in splitedTest:
        test2 = i.split('_')
        final += test2

    attributesName = [
        'MBERARBG Skilled labourers', 'MBERARBO Unskilled labourers', 'MSKA Social class A',
        'MSKB1 Social class B1', 'MSKB2 Social class B2', 'MSKC Social class C',
        'MSKD Social class D', 'MHHUUR Rented house', 'MHKOOP Home owners',
        'MAUT1 1 car', 'MAUT2 2 cars', 'MAUT0 No car'
    ]

    final_list = [int(i) for i in final]
    print(type(final_list))
    itemsetFinal = ""
    for i in range(1, len(final_list), 2):
        itemsetFinal += str(final_list[i - 1]) + "_ " + attributesName[final_list[i]] + ","
    # print(itemsetFinal)
    itemsetFinal = itemsetFinal[:-1]
    print(itemsetFinal)
    return itemsetFinal


def finalSupport(dic):
    lvl = 0
    finalDic = {}
    for x in dic:
        lvlCompared = str(x).count(',') + 1
        if lvl <= lvlCompared:
            finalDic[x] = dic[x]
            lvl = lvlCompared
        else:
            break
    return finalDic


######################################################################################

# this function is for prepare the lvl , parameters, support, supportArray
# inputs: finalDic is for the filtered Dictionary , dic is for the support array before filtering
# outputs: support for each rule, parameters array, lvl of the relation


def process(dic, finalDic, Min_confidence):
    lvl = 0
    for x in finalDic:
        support = finalDic[x]
        lvl = str(x).count(',') + 1
        tempArray = (str(x).split(','))
        parameterArrayString = tempArray
        # for y in tempArray:
        #     parameterArrayString += y.split('_')
        # parameterArrayInt = [int(i) for i in parameterArrayString]

        print("level is " + str(lvl))
        print("support is " + str(support))
        print("Rules for " + str(parameterArrayString) + " are")

        # confidence function call
        confidence(Min_confidence, parameterArrayString, support, dic)
        print()
    '''
        if lvl==1:
            for itemset in dic.keys():
                if itemset == x:
                    value = dic[itemset]
                    break
            confidence = support / value
            print("confidence is : " + str(confidence) + " = " + str(confidence * 100) + " %")
            print()
        else:
    '''


#######################################################################################

def concatenate_list_data(list):
    result = ''
    x = 1
    length = len(list)
    print(length)
    for element in list:
        if x < length:
            result = result + str(element) + ","
        else:
            result = result + str(element)
        x += 1
    return result


###########################################################################################

def generate_rules(itemset, confidence, parameterArrayString):
    after_imply = ''
    counter = 0
    length_parameterArray = len(parameterArrayString)
    # print(length_parameterArray)
    for element in parameterArrayString:

        for i in range(len(itemset)):
            if itemset[i] == element[0]:
                counter = counter + 1
                if i + 1 < len(itemset):
                    if itemset[i + 1] == element[1]:
                        counter = counter + 1
                        if i + 1 < len(itemset):
                            if itemset[i + 2] == element[2]:
                                counter = counter + 1
                                break

        if counter < 3:
            after_imply = after_imply + str(element) + ","

        counter = 0

    after_imply = after_imply.rstrip(',')
    # itemset names
    itemsetFinal = getNames(itemset)
    after_implyFinal = getNames(after_imply)

    print("The association rules is: " + itemsetFinal + " ---> " + after_implyFinal)
    print("confidence is : " + str(confidence) + " = " + str(confidence * 100) + " %")
    return after_imply


######################################################################################################

def lift(support, dic, value_left, after_imply):
    for item_key in dic.keys():
        if item_key == after_imply:
            Right = dic[item_key]
            break
    lift = (support / 5822) / ((value_left / 5822) * (Right / 5822))
    print("Lift of the rule is : " + str(lift))


###################################################################################################

def leverage(support, dic, value_left, after_imply):
    for item_key in dic.keys():
        if item_key == after_imply:
            value_right = dic[item_key]
            break
    leverage = (support / 5822) - ((value_left / 5822) * (value_right / 5822))
    print("Leverage of the rule is : " + str(leverage))


########################################################################################
def confidence(Min_confidence, parameterArrayString, support, dic):
    for L in range(1, len(parameterArrayString)):  # L : 3dd el items in one rule
        for subset in list(itertools.combinations(parameterArrayString, L)):  # generate rule for the specific L

            length_of_subset = len(subset)

            if length_of_subset == 1:
                x = subset[0]
                print(x + ":")

            else:
                x = concatenate_list_data(subset)
                print(x + ":")

            for itemset in dic.keys():
                if itemset == x:
                    value = dic[itemset]
                    break
            confidence = support / value
            # print(confidence)

            if (confidence > Min_confidence):
                after_imply = generate_rules(itemset, confidence, parameterArrayString)
                # print(after_imply)
                lift(support, dic, value, after_imply)
                leverage(support, dic, value, after_imply)
                print()
            else:
                print("confidence is : " + str(confidence) + " = " + str(confidence * 100) + " % " + "< Min Support")
##############################################################################################


