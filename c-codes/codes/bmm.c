/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-23 18:32:28
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-02 20:40:09
 */

#include <stdio.h>

int gcd(int a, int b) {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

int main(int argc, const char *argv[]) {
  int x, y;
  printf("Please Enter two number:");
  scanf("%d %d", &x, &y);
  printf("%d\n", gcd(x, y));

  return 0;
}
