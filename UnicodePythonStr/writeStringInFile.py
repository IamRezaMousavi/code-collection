# @Author: @IamRezaMousavi
# @Date:   2022-03-18 20:24:26
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-03-18 21:48:16


def main():
    fileName = 'writeStringInFile'
    string = (
        '\u067e\u06cc\u0631\u0648\u0632\u06cc \u0627\u0646\u0642\u0644\u0627\u0628 \u0627\u0633\u0644\u0627\u0645\u06cc'
    )

    string = '\u0645\u200c\u06cc'
    with open(fileName + '.txt', 'w', encoding='utf-8') as f:
        f.write(string)


if __name__ == '__main__':
    main()
