/**
 * @Author: S.Reza Mousavi
 * @Date:   2022-01-03 22:37:46
 * @Last Modified by:   S.Reza Mousavi
 * @Last Modified time: 2022-01-03 22:49:16
 */
#include <iostream>

using namespace std;

int main(int argc, const char *argv[]) {
  try {
    int numerator, denominator;
    cout << "Enter two number for Division:";
    cin >> numerator >> denominator;

    if (denominator == 0)
      throw 99;

    cout << "Result: " << (float)numerator / (float)denominator;
  } catch (int errorNumber) {
    cout << "Division by zero" << endl << "Error number is " << errorNumber << endl;
  }

  return 0;
}
