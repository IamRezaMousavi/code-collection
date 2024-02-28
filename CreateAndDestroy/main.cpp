/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-02 19:28:31
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2021-12-02 19:34:41
 */

#include "createAndDestroy.h"
#include <iostream>
using namespace std;

void             createObject();
createAndDestroy globalObject1(1), globalObject2(2);

int main(int argc, const char *argv[]) {
  createAndDestroy localObject1(3);
  cout << "This line will not be the firest line" << endl;
  createAndDestroy localObject2(4);
  createObject();
  return 0;
}

void createObject() {
  static createAndDestroy staticObject(5);
  createAndDestroy        automaticObject(6);
}
