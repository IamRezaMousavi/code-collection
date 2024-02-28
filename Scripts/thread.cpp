/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-03-08 23:45:15
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-03-08 23:49:56
 */

#include <iostream>
#include <thread>

using namespace std;

thread::id mainID = this_thread::get_id();

void printThreadId() {
  cout << this_thread::get_id() << endl;
}

int main(int argc, const char *argv[]) {
  cout << mainID << endl;

  thread t(printThreadId);

  cout << this_thread::get_id() << endl;

  t.join();
  return 0;
}
