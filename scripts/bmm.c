/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-23 18:32:28
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-09-25 17:39:08
 */
#include <conio.h>
#include <stdio.h>

int bmm(int num1, int num2);

int main(int argc, const char *argv[]) {
  int x, y;
  printf("Please Enter two number:");
  scanf("%d %d", &x, &y);

  printf("%d\n", bmm(x, y));

  getch();
  return 0;
}

int bmm(int num1, int num2) {
  int min     = (num1 < num2) ? num1 : num2;
  int enother = (num1 == min) ? num2 : num1;
  if (enother % min == 0) {
	return min;
  } else {
	int bmm = 1;
	for (int i = 2; i <= min / 2; i++) {
	  if ((min % i == 0) && (enother % i == 0)) {
		bmm = i;
		break;
	  }
	}
	return bmm;
  }
}
