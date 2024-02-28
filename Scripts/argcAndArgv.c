/**
 * @Author: S.Reza Mousavi
 * @Date:   2022-01-22 23:08:23
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2022-01-22 23:12:41
 */
#include <stdio.h>

int main(int counter, const char *arguments[]) {
  for (size_t item = 0; item < counter; item++)
    printf("arg[%d] = %s\n", item, arguments[item]);

  return 0;
}
