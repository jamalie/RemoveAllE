#   removeAll(e, L) takes in an element e and a list L.
#   Then, removeAll should return another list that is identical to L except that all elements identical to e have been removed.

def removeAll(e, L):
    newList = []

    for i in range(len(L)):
        if L[i] != e:
            newList.append(L[i])

    return newList

print removeAll(42, [ 55, 77, 42, 11, 42, 88 ])
print removeAll(42, [ 55, [77, 42], [11, 42], 88 ])
print removeAll([77, 42], [ 55, [77, 42], [11, 42], 88 ])
