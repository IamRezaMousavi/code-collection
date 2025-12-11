/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-16 17:18:37
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-12-11 16:51:12
 */

#include <iostream>

#include "testplusplus.hpp"

using namespace std;
const int RUN = 5;

void insertionSort(int array[], int left, int right) {
  for (size_t arrayIndex = left + 1; arrayIndex < right; arrayIndex++) {
    int temp = array[arrayIndex];
    int otherIndex = arrayIndex - 1;
    while (otherIndex >= left && array[otherIndex] > temp) {
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

void timSort(int array[], int left, int right) {
  for (size_t i = left; i < right; i += RUN) {
    int end = (i + RUN < right) ? i + RUN : right;
    insertionSort(array, i, end);
  }
  for (size_t RUNsize = RUN; RUNsize < right; RUNsize *= 2) {
    for (size_t start = left; start < right; start += 2 * RUNsize) {
      int middle = start + RUNsize;
      if (middle >= right)
        break;

      int end = (start + 2 * RUNsize < right) ? start + 2 * RUNsize : right;
      merge(array, start, middle, end);
    }
  }
}

void timSort(int array[], int arraySize) {
  timSort(array, 0, arraySize);
}

TEST(TimsortTestHandlesSingleElement) {
  int arr[] = {5};
  timSort(arr, 0, 1);
  ASSERT_EQ(arr[0], 5);
}

TEST(TimSortTestReverseArray) {
  int arr[] = {5, 4, 3, 2, 1};
  timSort(arr, 0, 5);
  ASSERT_EQ(arr[0], 1);
  ASSERT_EQ(arr[1], 2);
  ASSERT_EQ(arr[2], 3);
  ASSERT_EQ(arr[3], 4);
  ASSERT_EQ(arr[4], 5);
}

TEST(TimSortTestAlreadySorted) {
  int arr[] = {1, 2, 3, 4, 5};
  timSort(arr, 0, 5);
  int expected[] = {1, 2, 3, 4, 5};
  for (int i = 0; i < 5; i++)
    ASSERT_EQ(arr[i], expected[i]);
}

TEST(TimSortTestPartialRangeSort) {
  int arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};

  // [2, 8)
  timSort(arr, 2, 8);

  int expectedSorted[] = {3, 4, 5, 6, 7, 8};
  for (int i = 0; i < 6; i++)
    ASSERT_EQ(arr[i + 2], expectedSorted[i]);

  ASSERT_EQ(arr[0], 10);
  ASSERT_EQ(arr[1], 9);
  ASSERT_EQ(arr[8], 2);
  ASSERT_EQ(arr[9], 1);
}

TEST(TimSortTestSmallRunSize) {
  int arr[] = {4, 3, 2, 1};
  timSort(arr, 0, 4);

  int expected[] = {1, 2, 3, 4};
  for (int i = 0; i < 4; i++)
    ASSERT_EQ(arr[i], expected[i]);
}

TEST(TimSortTestMultiRunMerge) {
  int arr[] = {7, 6, 5, 4, 3, 2, 1, 0};
  timSort(arr, 0, 8);

  for (int i = 0; i < 8; i++)
    ASSERT_EQ(arr[i], i);
}

TEST(TimSortTestBoundaryMergeCase) {
  int arr[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
  timSort(arr, 0, 10);

  for (int i = 0; i < 10; i++)
    ASSERT_EQ(arr[i], i);
}

int main() {
  return testplusplus::runAllTests();
}
