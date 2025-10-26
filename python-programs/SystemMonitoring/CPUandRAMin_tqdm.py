# @Author: S.Reza Mousavi
# @Date:   2022-01-24 19:20:42
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2022-01-24 19:24:08


from time import sleep

import psutil
from tqdm import tqdm


def main():
    with (
        tqdm(total=100, desc='CPU%', position=1) as cpubar,
        tqdm(
            total=100,
            desc='RAM%',
            position=0,
        ) as rambar,
    ):
        while True:
            rambar.n = psutil.virtual_memory().percent
            cpubar.n = psutil.cpu_percent()
            rambar.refresh()
            cpubar.refresh()
            sleep(0.1)


if __name__ == '__main__':
    main()
