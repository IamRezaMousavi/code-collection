/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-12-20 14:07:15
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-10-28 01:37:41
 */

#define _GNU_SOURCE

#include <math.h>
#include <stddef.h>

double dot(const double *array1, const double *array2, size_t n) {
  if (!array1 || !array2 || n == 0)
    return 0.0;
  double sum = 0.0;
  for (size_t i = 0; i < n; i++) {
    sum += array1[i] * array2[i];
  }
  return sum;
}

double circle_area(double r) {
    return M_PI * r * r;
}

double pi(void) {
    return M_PI;
}
