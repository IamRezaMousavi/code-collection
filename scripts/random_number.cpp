/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-15 11:41:55
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2021-12-30 21:53:16
 */
#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

int main(int argc, const char *argv[]) {
  srand(time(0));

  int start = 0, stop = 10;

  cout << start + (rand() % stop) << endl;

  return 0;
}
