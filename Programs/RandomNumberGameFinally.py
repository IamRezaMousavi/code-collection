"""Created on Sat May 29 21:41:46 2021

@author: Mohammad
"""

import random

print('سلام، خوش آمدید')
print('بیاید بازی کنیم')
print('من یک عدد انتخاب میکنم شما حدس بزن')

edame = ''
while edame != 'n':
    print('بگوعدد چند رقمی انتخاب کنم؟', end='')
    ragham = int(input())
    add = random.randint(10 ** (ragham - 1), 10**ragham)
    # print(add)

    while edame != 'n':
        print('یک حدس بزن:', end=' ')
        hads = int(input())

        if hads == add:
            print('**********************************************')
            print('***بریک میگم! شما عدد انتخابی را پیدا کردید***')
            print('**********************************************')
            break

        else:
            print('متاسفانه درست نیست.', end=' ')

            if hads < add:
                print('عدد انتخابی ما بزرگتر است')

            elif hads > add:
                print('عدد انتخابی ما کوچکتر است.')

        edame = input('میخواهید دوباره امتحان کنید؟(y/n)')
    if edame != 'n':
        edame = input('میخواهید بازم بازی کنید؟(y/n)')

# Edited on Sat May 29 21:33:00 2021
