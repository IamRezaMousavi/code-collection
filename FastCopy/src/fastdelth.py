# @Author: @IamRezaMousavi
# @Date:   2022-09-04 14:58:00
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-09-04 19:57:19

import argparse
import glob
import logging
import os
import threading
from datetime import datetime
from queue import Queue

from human_time import human_time


def b2h(fileSize, unit='B', unitDivisor=1024):
    for prefix in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(fileSize) < unitDivisor:
            return f'{fileSize:3.2f} {prefix}{unit}'

        fileSize /= unitDivisor

    return f'{fileSize:3.2f} Y{unit}'


def isEmpty(dirPath):
    return os.listdir(dirPath) == []


def deletePath(q: Queue, path: str, filesSize: Queue):
    try:
        if not os.path.exists(path):
            return

        if isEmpty(path):
            os.rmdir(path)
            logging.info(f'remove {path}')
            print(f'Remove {path}')
        else:
            for sub in os.listdir(path):
                subPath = os.path.join(path, sub)
                if os.path.isfile(subPath):
                    size = filesSize.get()
                    size += os.path.getsize(subPath)
                    filesSize.put(size)

                    os.remove(subPath)
                    print(f'delete {subPath}')
                    logging.info(f'delete {subPath}')
                elif isEmpty(subPath):
                    os.rmdir(subPath)
                    logging.info(f'remove {subPath}')
                    print(f'Remove {subPath}')
                else:
                    q.put(subPath)
        if isEmpty(path):
            os.rmdir(path)
            logging.info(f'remove {path}')
            print(f'Remove {path}')
        else:
            q.put(path)

    except Exception as e:
        logging.exception(e)
        print(e)


def worker(q: Queue, filesSize: Queue):
    while not q.empty():
        path = q.get()

        deletePath(q, path, filesSize)

        q.task_done()


def main():
    if not os.path.exists('log'):
        os.mkdir('log')

    logging.basicConfig(
        filename='log/fastdelth.log',
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    parser = argparse.ArgumentParser(description='Fast Tree File Delete.')
    parser.add_argument('path', type=str, nargs='+', help='Path')

    args = parser.parse_args()
    logging.debug(f'get args: path={args.path}')

    startTime = datetime.now()
    THREAD_NUMBER = os.cpu_count()

    filesSize = Queue()
    filesSize.put(0)

    paths = Queue()
    for path in args.path:
        for top in glob.glob(path):
            for root, dirs, files in os.walk(top):
                paths.put(root)
                print('puts:', root)

    print('\n+++++++++++++++++++++++\n')

    for _ in range(THREAD_NUMBER):
        threading.Thread(target=worker, args=(paths, filesSize)).start()

    paths.join()
    t = datetime.now() - startTime
    print('Get', b2h(filesSize.get()))
    print('Done in', human_time(t.seconds))


if __name__ == '__main__':
    main()
