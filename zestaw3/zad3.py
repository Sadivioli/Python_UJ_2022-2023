
#iterative function to reverse list in place from leftInxed to rightIndex
def reverseList(list1, leftInxed, rightIndex):
    if rightIndex < leftInxed:
        leftInxed, rightIndex = rightIndex, leftInxed
    while leftInxed < rightIndex:
        list1[leftInxed], list1[rightIndex] = list1[rightIndex], list1[leftInxed]
        leftInxed += 1
        rightIndex -= 1
    return list1

#recursive function to reverse list in place from leftInxed to rightIndex
def reverseListRec(list1, leftInxed, rightIndex):
    if leftInxed < rightIndex:
        list1[leftInxed], list1[rightIndex] = list1[rightIndex], list1[leftInxed]
        reverseListRec(list1, leftInxed + 1, rightIndex - 1)
    return list1

list1 = ["L", "O", "R", "E", "M", " ", "I", "P", "S", "U", "M"]
list2 = ["L", "O", "R", "E", "M", " ", "I", "P", "S", "U", "M"]
leftInxed = 1
rightIndex = 7

print(reverseList(list1, leftInxed, rightIndex))
print(reverseListRec(list2, leftInxed, rightIndex))