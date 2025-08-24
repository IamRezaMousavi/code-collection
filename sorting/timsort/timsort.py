# @Author: S.Reza Mousavi
# @Date:   2022-01-02 03:17:13
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2022-01-02 03:46:48


RUN = 5


def InsertionSort(arr):
    for x in range(1, len(arr)):
        for i in range(x, 0, -1):
            if arr[i] < arr[i - 1]:
                t = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = t
            else:
                break
            i = i - 1
    return arr


def Merge(aArr, bArr):
    a = b = 0
    cArr = []

    while a < len(aArr) and b < len(bArr):
        if aArr[a] < bArr[b]:
            cArr.append(aArr[a])
            a += 1
        elif bArr[b] < aArr[a]:
            cArr.append(bArr[b])
            b += 1
        else:
            cArr.append(aArr[a])
            cArr.append(bArr[b])
            a, b = a + 1, b + 1
    while a < len(aArr):
        cArr.append(aArr[a])
        a += 1
    while b < len(bArr):
        cArr.append(bArr[b])
        b += 1
    return cArr


def TimSort(arr, n):
    for x in range(0, n, RUN):
        arr[x : x + RUN] = InsertionSort(arr[x : x + RUN])

    RUNinc = RUN
    while RUNinc < n:
        for x in range(0, n, RUNinc * 2):
            arr[x : x + 2 * RUNinc] = Merge(
                arr[x : x + RUNinc],
                arr[x + RUNinc : RUNinc * 2],
            )
        RUNinc *= 2
    return arr


arr = list(range(12, 1, -1))
arr = TimSort(arr, len(arr))
print(arr)
