/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-01-02 03:47:37
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-09-25 17:58:11
 */
#include <iostream>

using namespace std;
const int RUN = 5;

void insertionSort(int array[], int left, int right);
void merge(int array[], int left, int middle, int right);
void timSort(int array[], int arraySize);
void timSort(int array[], int left, int right);
void printArray(int array[], int arraySize);
void printArray(int array[], int left, int right);

int main(int argc, const char *argv[]) {
  int arraySize = 23;
  int array[arraySize];
  for (size_t i = 0; i < arraySize; i++)
	array[i] = arraySize - i;
  printArray(array, arraySize);
  timSort(array, 2, arraySize - 2);
  printArray(array, arraySize);
  return 0;
}

void insertionSort(int array[], int left, int right) {
  for (size_t arrayIndex = left + 1; arrayIndex < right; arrayIndex++) {
	int temp       = array[arrayIndex];
	int otherIndex = arrayIndex - 1;
	while (array[otherIndex] > temp && otherIndex >= left) {
	  array[otherIndex + 1] = array[otherIndex];
	  otherIndex--;
	}
	array[otherIndex + 1] = temp;
  }
}

void merge(int array[], int left, int middle, int right) {
  int leftIndex = 0, rightIndex = 0, arrayIndex = left;
  int leftSize = middle - left, rightSize = right - middle;
  int leftArray[leftSize], rightArray[rightSize];

  for (size_t i = 0; i < leftSize; i++)
	leftArray[i] = array[left + i];
  for (size_t i = 0; i < rightSize; i++)
	rightArray[i] = array[middle + i];

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

void timSort(int array[], int arraySize) {
  for (size_t i = 0; i < arraySize; i += RUN) {
	int end = (i + RUN < arraySize) ? i + RUN : arraySize;
	insertionSort(array, i, end);

	cout << "After InsertionSort " << i << ": ";
	printArray(array, arraySize);
  }
  for (size_t RUNsize = RUN; RUNsize < arraySize; RUNsize *= 2) {
	for (size_t start = 0; start < arraySize; start += 2 * RUNsize) {
	  int middle = start + RUNsize;
	  if (middle >= arraySize) break;

	  int end = (start + 2 * RUNsize < arraySize) ? start + 2 * RUNsize : arraySize;
	  merge(array, start, middle, end);

	  cout << "After Merge " << start << " in RUNsize " << RUNsize << ": ";
	  printArray(array, arraySize);
	}
  }
}

void timSort(int array[], int left, int right) {
  for (size_t i = left; i < right; i += RUN) {
	int end = (i + RUN < right) ? i + RUN : right;
	insertionSort(array, i, end);

	cout << "After InsertionSort " << i << ": ";
	printArray(array, left, right);
  }
  for (size_t RUNsize = RUN; RUNsize < right; RUNsize *= 2) {
	for (size_t start = left; start < right; start += 2 * RUNsize) {
	  int middle = start + RUNsize;
	  if (middle >= right) break;

	  int end = (start + 2 * RUNsize < right) ? start + 2 * RUNsize : right;
	  merge(array, start, middle, end);

	  cout << "After Merge " << start << " in RUNsize " << RUNsize << ": ";
	  printArray(array, left, right);
	}
  }
}

void printArray(int array[], int arraySize) {
  for (size_t index = 0; index < arraySize; index++)
	cout << array[index] << " ";
  cout << endl;
}

void printArray(int array[], int left, int right) {
  for (size_t index = left; index < right; index++)
	cout << array[index] << " ";
  cout << endl;
}
