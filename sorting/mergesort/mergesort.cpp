/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-16 17:18:37
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2021-12-17 01:26:37
 */
#include <iostream>

using namespace std;

void merge(int array[], int left, int mid, int right);
void mergeSort(int array[], int begin, int end);

int main(int argc, const char *argv[]) {
  int array[]   = {10, 8, 5, -2, 17, 15, 22, -4};
  int arraySize = sizeof(array) / sizeof(array[0]);

  for (size_t i = 0; i < arraySize; i++)
	cout << array[i] << " ";
  cout << endl;

  mergeSort(array, 0, arraySize); // array[begin:end]

  for (size_t i = 0; i < arraySize; i++)
	cout << array[i] << " ";

  return 0;
}

void merge(int array[], int left, int mid, int right) {
  int leftIndex = 0, rightIndex = 0, arrayIndex = left;
  int leftSize = mid - left, rightSize = right - mid;
  int leftArray[leftSize], rightArray[rightSize];

  for (size_t i = 0; i < leftSize; i++)
	leftArray[i] = array[left + i];
  for (size_t i = 0; i < rightSize; i++)
	rightArray[i] = array[mid + i];

  while (leftIndex < leftSize && rightIndex < rightSize) {
	if (leftArray[leftIndex] <= rightArray[rightIndex]) {
	  array[arrayIndex] = leftArray[leftIndex];
	  leftIndex++;
	} else {
	  array[arrayIndex] = rightArray[rightIndex];
	  rightIndex++;
	}
	arrayIndex++;
  }

  while (leftIndex < leftSize) {
	array[arrayIndex] = leftArray[leftIndex];
	leftIndex++;
	arrayIndex++;
  }
  while (rightIndex < rightSize) {
	array[arrayIndex] = rightArray[rightIndex];
	rightIndex++;
	arrayIndex++;
  }
}

void mergeSort(int array[], int begin, int end) {
  if (end - begin == 1) return;

  int mid = (end + begin) / 2;

  mergeSort(array, begin, mid); // left = array[begin:mid]
  mergeSort(array, mid, end);   // right = array[mid:end]
  merge(array, begin, mid, end);
}
