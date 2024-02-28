/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-11-27 19:42:56
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2021-11-27 20:06:24
 */

#include <stdio.h>

void first(int i, int n) {
  for (size_t j = 1; j < i + 1; j++)
    printf("%d", j);
  for (size_t j = 1; j < (n - i) + 1; j++)
    printf(" ");
}

void second(int i, int n) {
  for (size_t j = 1; j < (n - i) + 1; j++)
    printf(" ");
  for (size_t j = i; j > 0; j--)
    printf("%d", j);
}

int main(int argc, const char *argv[]) {
  int n = 0;
  printf("Please enter n:");
  scanf("%d", &n);
  for (size_t i = 0; i < n + 1; i++) {
    first(i, n);
    second(i, n);
    printf("\n");
  }

  return 0;
}
