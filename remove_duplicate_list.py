import collections


def return_unique(lst):
    return list(set(lst))


# merge
print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))

#remove duplicate (just display unique list)
ls1 = [1, 9, 8, 8, 7, 6, 1, 6]
ls2 = [item for item, count in collections.Counter(ls1).items() if count > 1]

print(list(set(ls1) - set(ls2)))
