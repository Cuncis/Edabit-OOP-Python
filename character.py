def to_dict(lst):
    myDict = {}
    val = 0
    res = [ord(ele) for sub in lst for ele in sub]

    for i in lst:
        val += 1
        myDict[i] = res[val-1]
    return myDict


print(to_dict(["a", "b", "c"]))