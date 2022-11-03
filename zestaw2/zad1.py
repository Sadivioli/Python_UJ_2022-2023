

list1 = [1, 2, [3, 4, [5, 6], 5], 3, [4, 5]]
list2 = [1, [2, 3], 4]
list3 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
list4 = [1, [3], [2]]
value1 = 19
value2 = 13
value3 = 69
value4 = 33


#finds the deepest list in the list
def deepest_lists(lst, nest):

    global deepCount
    global deeepestList

    for i in lst:
        if type(i) is list:
            deepest_lists(i, nest+1)
    
    if nest > deepCount:
        deepCount = nest
        deeepestList = []
        deeepestList.append(lst)

    elif nest == deepCount:
        deeepestList.append(lst)

    return deeepestList
    

def main(list, value):
    global deeepestList
    global deepCount
    deeepestList = []
    deepCount = 0

    deepest_lists(list, 0)

    for i in deeepestList:
        i.append(value)
    
    print(list)



print(list1, " inserting: ", value1, "---->")   
main(list1,value1)
print(list2, " inserting: ", value2, "---->")
main(list2,value2)
print(list3, " inserting: ", value3, "---->")
main(list3,value3)
print(list4, " inserting: ", value4, "---->")
main(list4,value4)