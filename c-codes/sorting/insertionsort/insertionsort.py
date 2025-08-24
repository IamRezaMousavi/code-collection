# @Author: @IamRezaMousavi
# @Date:   2021-12-17 16:01:00
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2021-12-17 16:06:03


_list = [2, 9, -5, 10, 8]

for i in range(1, len(_list)):
    for j in range(i):
        if _list[i] < _list[j]:
            _list.insert(j, _list.pop(i))

print(_list)
