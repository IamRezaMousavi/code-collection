/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-02 19:25:49
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2021-12-02 19:28:22
 */

#include "createAndDestroy.h"
#include <iostream>
using namespace std;

createAndDestroy::createAndDestroy(int id) {
  cout << "Initializing " << id << endl;
  which = id;
}

createAndDestroy::~createAndDestroy() {
  cout << "Destroying " << which << endl;
  cin.get();
}