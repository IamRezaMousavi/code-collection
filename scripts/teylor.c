/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-05 21:13:53
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2021-12-05 22:41:48
 */

#include <stdio.h>

#define SIN 0
#define COS 1

int main(int argc, const char *argv[]) {
  int   n;
  float x, error = 0.0001, sum = 0;

  printf("N: 0 for sin, 1 for cos\n");
  printf("Please enter n and x:");
  scanf("%d %f", &n, &x);

  int sign = 1, count = 1;

  if (n == SIN) {
	float        numerator = x;
	unsigned int factorial = 1;
	float        sinx      = numerator / factorial;
	sign                   = (count % 2 == 0) ? -1 : 1;
	do {
	  sum       += sign * sinx;
	  numerator *= x * x;
	  count++;
	  factorial *= (2 * count - 1) * (2 * count - 2);
	  sinx       = numerator / factorial;
	  sign       = (count % 2 == 0) ? -1 : 1;
	} while (sinx > error);
  }

  else if (n == COS) {
	sum = 1;

	count++;
	float        numerator = x * x;
	unsigned int factorial = 2;
	float        cosx      = numerator / factorial;
	sign                   = (count % 2 == 0) ? -1 : 1;
	do {
	  sum       += sign * cosx;
	  numerator *= x * x;
	  count++;
	  factorial *= (2 * count - 3) * (2 * count - 2);
	  cosx       = numerator / factorial;
	  sign       = (count % 2 == 0) ? -1 : 1;
	} while (cosx > error);
  }

  printf("%.4f\n", sum);

  return 0;
}
