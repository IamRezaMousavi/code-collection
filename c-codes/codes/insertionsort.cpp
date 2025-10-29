/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-17 16:37:24
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2022-01-02 05:15:56
 */
#include <iostream>

using namespace std;

void insertionSort(int array[], int left, int right);

int main(int argc, const char *argv[]) {
  int array[] = {2, 9, -5, 10, 8};
  int arraySize = sizeof(array) / sizeof(array[0]);

  insertionSort(array, 0, arraySize);

  for (size_t i = 0; i < arraySize; i++)
    cout << array[i] << " ";

  return 0;
}

void insertionSort(int array[], int left, int right) {
  for (size_t i = left + 1; i < right; i++) {
    int temp = array[i];
    int j = i - 1;
    while (temp < array[j] && j >= left) {
      array[j + 1] = array[j];
      j--;
    }
    array[j + 1] = temp;
  }
}
