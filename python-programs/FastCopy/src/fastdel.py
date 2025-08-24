# @Author: @IamRezaMousavi
# @Date:   2022-05-25 02:44:05
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-07-23 23:40:07

import argparse
import glob
import logging
import os
import shutil
import time


def b2h(fileSize, unit='B', unitDivisor=1024):
    for prefix in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(fileSize) < unitDivisor:
            return f'{fileSize:3.2f} {prefix}{unit}'

        fileSize /= unitDivisor

    return f'{fileSize:3.2f} Y{unit}'


def main():
    logging.basicConfig(
        filename='log/fastdel.log',
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    parser = argparse.ArgumentParser(description='Fast Tree File Delete.')
    parser.add_argument('path', type=str, nargs='+', help='Path')

    args = parser.parse_args()
    logging.debug(f'get args: path={args.path}')

    startTime = time.time()
    filesSize = 0
    for path in args.path:
        for top in glob.glob(path):
            if not os.path.isdir(top):
                continue
            for root, dirs, files in os.walk(top, topdown=False):
                for file in files:
                    path = os.path.join(root, file)
                    filesSize += os.path.getsize(path)
                    os.remove(path)
                    logging.info(f'delete {path}')

                shutil.rmtree(root)
                logging.info(f'remove {root}')
                print(f'Remove {root}')
    print(f'Get {b2h(filesSize)}')
    print(f'In {time.time() - startTime:.2f} s')


if __name__ == '__main__':
    main()
