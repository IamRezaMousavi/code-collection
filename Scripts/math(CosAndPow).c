/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-23 18:32:28
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 21:17:59
 */
#include <conio.h>
#include <math.h>
#include <stdio.h>

int main(int argc, const char *argv[]) {
  for (double i = -1.0; i <= 1.0; i += 0.1)
    printf("Cos(%.1f) = %.4f\n", i, cos(i));
  printf("\n==============\n");

  for (double i = 1; i < 366; i++)
    printf("1.01^%.1f\t%f\n", i, pow(1.01, i));

  getch();
  return 0;
}
