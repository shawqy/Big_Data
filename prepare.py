

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


# this function is for prepare the lvl , parameters, support, supportArray
# inputs: finalDic is for the filtered Dictionary , dic is for the support array before filtering
# outputs: support for each rule, parameters array, lvl of the relation
def process(finalDic, dic):
    lvl = 0
    for x in finalDic:
        support = finalDic[x]
        lvl = str(x).count(',') + 1
        tempArray = (str(x).split(','))
        parameterArrayString = []
        for y in tempArray:
            parameterArrayString += y.split('_')
        parameterArrayInt = [int(i) for i in parameterArrayString]

        # confidence function call
        # confidence(lvl, parameterArrayInt, support, dic)