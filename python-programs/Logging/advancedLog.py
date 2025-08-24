# @Author: @IamRezaMousavi
# @Date:   2022-04-14 06:06:05
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-04-14 06:15:55

import logging


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s'))

    fi = logging.FileHandler('log/advance.log')
    fi.setLevel(logging.DEBUG)
    fi.setFormatter(logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s'))

    logger.addHandler(ch)
    logger.addHandler(fi)
    logger.debug('%s %i', 'Number:', 15)


if __name__ == '__main__':
    main()
