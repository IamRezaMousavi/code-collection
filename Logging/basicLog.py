# @Author: @IamRezaMousavi
# @Date:   2022-04-14 05:30:15
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-04-14 06:28:57

import logging


def main():
    logging.basicConfig(
        filename='log/basic.log',
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    logging.debug('this massage is debug')
    logging.warning('WHATCH Out!')
    logging.info('I told you')


if __name__ == '__main__':
    main()
