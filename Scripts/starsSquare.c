/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-19 00:16:43
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-09-25 17:50:25
 */
#include <stdio.h>

int main(int argc, const char *argv[]) {
  int a, b;
  scanf("%d %d", &a, &b);

  int difference = a - b;

  for (size_t row = 0; row < a; row++) {
    for (size_t column = 0; column < a; column++) {
      if (row >= difference / 2 && row < a - (difference / 2) && column >= difference / 2
          && column < a - (difference / 2)) {
        printf("  ");
      } else {
        printf("* ");
      }
    }
    printf("\n");
  }

  return 0;
}
