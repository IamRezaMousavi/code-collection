/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-23 18:32:28
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-02 20:48:12
 */
#include <stdio.h>

int gcm(int a, int b) {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

int lcm(int a, int b) {
  /*
                a * b
  LCM(a, b) = -----------
               gcm(a, b)
  */
  return a / gcm(a, b) * b;
}

int main(int argc, const char *argv[]) {
  int x, y;
  printf("Please Enter two number:");
  scanf("%d %d", &x, &y);

  printf("%d\n", lcm(y, x));

  return 0;
}
