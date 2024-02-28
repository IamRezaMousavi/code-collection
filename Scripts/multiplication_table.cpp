/**
 * @Author: S.Reza Mousavi
 * @Date:   2021-12-23 18:32:28
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 21:20:27
 */
#include <iostream>
using namespace std;

int main(int argc, const char *argv[]) {
  cout << "Ya Allah" << endl;
  cout << "Hello C++" << endl;

  int rows = 0, columns = 0;
  cout << "Please enter rows and columns:";
  cin >> rows >> columns;

  for (size_t i = 1; i <= rows; i++) {
    for (size_t j = 1; j <= columns; j++)
      cout << i * j << "\t";
    cout << endl;
  }

  return 0;
}
