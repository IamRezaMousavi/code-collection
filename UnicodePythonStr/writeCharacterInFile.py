# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-03-18 20:24:26
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-03-18 20:34:04


def main():
    fileName = "writeCharacterInFile"
    character = u"\u067e"
    with open(fileName + ".txt", "w", encoding="utf-8") as f:
        f.write(character)


if __name__ == "__main__":
    main()
