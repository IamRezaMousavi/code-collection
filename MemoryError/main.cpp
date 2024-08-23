/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-03-06 23:37:28
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-03-07 00:19:21
 */

#include "memory.h"
#include <iostream>

using namespace std;

int main(int argc, const char *argv[]) {
  MyString hello("HELLO");

  { MyString copy = hello; }

  hello = hello;

  cout << hello.getString() << endl;

  return 0;
}
