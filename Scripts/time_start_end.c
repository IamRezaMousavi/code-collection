/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-30 22:38:41
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 22:59:47
 */
#include <stdio.h>
#include <time.h>

/*
For Time Difference

int main(int argc, char const *argv[])
{
    time_t start, end;
    start = time(NULL);

    int count = 100000;
    for (size_t i = 0; i < count; i++)
    {
        printf("%d\n", i);
    }

    end = time(NULL);

    printf("Time: %fs", difftime(end, start));
    return 0;
}
*/

// For Find Clock Ticks
int main(int argc, const char *argv[]) {
  clock_t t = clock();

  int count = 100000;
  for (size_t i = 0; i < count; i++)
    printf("%d\n", i);

  t = clock() - t;
  printf("No. of clicks %ld clicks (%f seconds).\n", t, ((float)t) / CLOCKS_PER_SEC);

  return 0;
}
