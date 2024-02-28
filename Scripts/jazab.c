/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-18 20:22:47
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2021-12-18 21:52:32
 */
#include <math.h>
#include <stdio.h>

void jazab(int array[], int number);

int main(int argc, const char *argv[]) {
  int n = 0;
  printf("Please enter n:");
  scanf("%d", &n);

  int result[n], resultIndex = 1, number = 31;

  result[0] = 30;
  while (resultIndex < n) {
    int array[] = {0, 0, 0};
    jazab(array, number);
    if (array[2] != 0) {
      result[resultIndex] = number;
      resultIndex++;
    }
    number++;
  }

  for (size_t i = 0; i < n; i++)
    printf("%d ", result[i]);

  return 0;
}

void jazab(int array[], int number) {
  int arrayIndex = 0;
  while (number % 2 == 0 && arrayIndex < 3) {
    array[arrayIndex] = 2;
    number /= 2;
  }

  arrayIndex = (array[arrayIndex] != 0) ? arrayIndex + 1 : arrayIndex;

  for (size_t i = 3; i <= sqrt(number); i += 2) {
    while (number % i == 0 && arrayIndex < 3) {
      array[arrayIndex] = i;
      number /= i;
    }
    arrayIndex = (array[arrayIndex] != 0) ? arrayIndex + 1 : arrayIndex;
  }

  if (number > 2 && arrayIndex < 3)
    array[arrayIndex] = number;
}