# @Author: @IamRezaMousavi
# @Date:   2022-03-20 22:45:19
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-03-20 23:00:01

import hashlib


def hashCode(data: str):
    hash = hashlib.sha256()
    hash.update(data.encode('utf-8'))
    return hash.hexdigest()


data = 'IamRezaMousavi'
print('\t', hashCode(data))
