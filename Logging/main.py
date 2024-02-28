# @Author: @IamRezaMousavi
# @Date:   2022-04-14 06:22:21
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-04-14 06:29:18

import logging

import mylib

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logHandler = logging.FileHandler('log/project.log')
logHandler.setLevel(logging.DEBUG)
logHandler.setFormatter(
    logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s', datefmt='%Y-%m-%d %H:%M:%S'),
)
logger.addHandler(logHandler)


def main():
    logger.info('Start Main')
    mylib.doSomething()
    logger.info('Main Ended')


if __name__ == '__main__':
    main()
