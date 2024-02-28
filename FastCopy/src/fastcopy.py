# @Author: @IamRezaMousavi
# @Date:   2022-05-24 23:43:58
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-05-25 04:18:09

import argparse
import glob
import logging
import os
import shutil
import threading


def copyFile(src, dest):
    shutil.copy2(src, dest)
    logging.info(f'copy {src} to {dest}')


def moveFile(src, dest):
    shutil.move(src, dest)
    logging.info(f'move {src} to {dest}')


def main():
    logging.basicConfig(
        filename='log/fastcopy.log',
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    parser = argparse.ArgumentParser(description='Fast File Copy.')
    parser.add_argument('src', type=str, nargs='+', help='Source File')
    parser.add_argument('dest', type=str, nargs=1, help='Destination File')
    parser.add_argument(
        '--move',
        dest='func',
        action='store_const',
        const=moveFile,
        default=copyFile,
        help='Move File',
    )

    args = parser.parse_args()
    logging.debug(f'get args: src={args.src} dest={args.dest}')

    src = args.src
    dest = args.dest[0]
    act = args.func.__name__[:4].title()

    THREAD_LIMIT = os.cpu_count() if os.cpu_count() else 4
    threads = []
    fileNames = []
    for s in src:
        for file in glob.glob(s):
            t = threading.Thread(target=args.func, args=(file, dest))
            t.start()
            threads.append(t)
            fileNames.append(file)

            while threading.active_count() > THREAD_LIMIT:
                threads[0].join()
                print(f'{act} {fileNames[0]} to {dest}')
                threads.pop(0)
                fileNames.pop(0)

    while threads:
        threads[0].join()
        print(f'{act} {fileNames[0]} to {dest}')
        threads.pop(0)
        fileNames.pop(0)


if __name__ == '__main__':
    main()
