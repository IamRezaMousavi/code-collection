/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-16 00:53:56
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2021-12-16 01:23:07
 */
#include <chrono>
#include <cmath>
#include <iostream>

unsigned __int64 getMicroseconds();

int main(int argc, const char *argv[]) {
  unsigned __int64 start = getMicroseconds();
  std::cout << "Start = " << start << std::endl;

  // Write your code

  unsigned __int64 now = getMicroseconds();
  std::cout << "Now = " << now << std::endl;
  std::cout << (now - start) * pow(10, -6) << " s" << std::endl;

  return 0;
}

unsigned __int64 getMicroseconds() {
  return std::chrono::duration_cast<std::chrono::microseconds>(
             std::chrono::system_clock::now().time_since_epoch()
  )
      .count();
}
