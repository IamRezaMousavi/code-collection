# @Author: @IamRezaMousavi
# @Date:   2021-12-16 03:26:20
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2021-12-16 03:42:27


def merge(list1, list2):
    sizeList1 = len(list1)
    sizeList2 = len(list2)
    _list = []

    i = j = 0
    while i < sizeList1 and j < sizeList2:
        if list1[i] < list2[j]:
            _list.append(list1[i])
            i += 1
        else:
            _list.append(list2[j])
            j += 1
    _list += list1[i:]
    _list += list2[j:]
    return _list


def mergeSort(_list):
    if len(_list) == 1:
        return _list
    mid = len(_list) // 2
    right = mergeSort(_list[mid:])
    left = mergeSort(_list[:mid])
    return merge(right, left)


print(mergeSort([1, 0, 2, 4, 5, -2, -11, 7, 11]))
