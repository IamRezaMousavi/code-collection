/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-05 21:13:53
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-08 11:05:00
 */
#include <math.h>
#include <stdio.h>

#define EPSILON 1e-6
#define DEG_TO_RAD(x) ((x) * M_PI / 180.0)

/*
-----------------------------------------------

          x^1     x^3     x^5     x^7
sin(x) = ----- - ----- + ----- - ----- + ...
          1!      3!      5!      7!


term_k = (-1)^k * x^(2k+1) / (2k+1)!
-----------------------------------------------
*/
double taylor_sin(double x) {
  double term = x;
  double sum = term;
  int k = 1;

  while (fabs(term) > EPSILON) {
    term *= -1 * x * x / ((2 * k) * (2 * k + 1));
    sum += term;
    k++;
  }
  return sum;
}

/*
-----------------------------------------------

          x^0     x^2     x^4     x^6
cos(x) = ----- - ----- + ----- - ----- + ...
          0!      2!      4!      6!


term_k = (-1)^k * x^(2k) / (2k)!
-----------------------------------------------
*/
double taylor_cos(double x) {
  double term = 1.0;
  double sum = term;
  int k = 1;

  while (fabs(term) > EPSILON) {
    term *= -1 * x * x / ((2 * k - 1) * (2 * k));
    sum += term;
    k++;
  }
  return sum;
}

int main(int argc, const char *argv[]) {
  double degrees;
  printf("Enter angle in degrees: ");
  scanf("%lf", &degrees);

  double x = DEG_TO_RAD(degrees);

  double sin_val = taylor_sin(x);
  double cos_val = taylor_cos(x);

  printf("\nUsing Taylor Series (ε = %.1e):\n", EPSILON);
  printf("sin(%.2f°) ≈ %.6f\n", degrees, sin_val);
  printf("cos(%.2f°) ≈ %.6f\n", degrees, cos_val);

  printf("\nUsing math.h for comparison:\n");
  printf("sin(%.2f°) = %.6f\n", degrees, sin(x));
  printf("cos(%.2f°) = %.6f\n", degrees, cos(x));

  return 0;
}
