/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-23 18:32:28
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 21:15:01
 */
#include <stdio.h>

int kmm(int num1, int num2);

int main(int argc, const char *argv[]) {
  int x, y;
  printf("Please Enter two number:");
  scanf("%d %d", &x, &y);

  printf("%d\n", kmm(y, x));

  return 0;
}

int kmm(int num1, int num2) {
  int max     = (num1 > num2) ? num1 : num2;
  int enother = (num1 == max) ? num2 : num1;

  if (max % enother == 0) {
	return max;
  } else {
	int number = max;
	int count  = 2;
	while (number % enother != 0) {
	  number = max * count;
	  count++;
	}
	return number;
  }
}
