/**
 * @Author: @IamRezaMousavi
 * @Date:   1970-01-01 03:30:00
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-09-25 17:44:20
 */
#include <stdarg.h>
#include <stdio.h>

void printArgs(int arg1, ...) {
  va_list valist;

  va_start(valist, arg1);
  for (int i = arg1; i > 0; i = va_arg(valist, int))
    printf("%d ", i);
  va_end(valist);
  printf("\n");
}

int main() {
  printArgs(3, 7, 8, 9, 2, 3, -1);
  return 0;
}
