/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-02 17:25:09
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-09-25 17:45:26
 */
#include <iostream>
using namespace std;

template <typename T>
T maximum(T p1, T p2, T p3);

int main(int argc, const char *argv[]) {
  int i1 = 10, i2 = 20, i3 = 30;
  cout << maximum(i1, i2, i3) << endl;

  cin.get();
  return 0;
}

template <typename T>
T maximum(T p1, T p2, T p3) {
  T max;
  max = (p1 > p2) ? p1 : p2;
  max = (p3 > max) ? p3 : max;
  return max;
}
