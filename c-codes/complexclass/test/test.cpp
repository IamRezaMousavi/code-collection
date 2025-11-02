/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-04 18:57:31
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-02 22:00:57
 */

#include <cassert>
#include <iostream>

#include "Complex.hpp"

void test_complex(void) {
  assert(Complex(4, 1) + Complex(1, 4) == Complex(5, 5));
  assert(Complex(4, 1) - Complex(1, 4) == Complex(3, -3));
  assert(J * J == Complex(-1));
  assert(Complex(1) / J == Complex(-1) * Complex(0, 1));

  Complex number(2, 2);
  assert(Complex::fromPolar(number.radial(), number.angular()) == number);
  assert(ComplexMath::pow(number, 2) == Complex(0, 8));
}

int main(int argc, const char *argv[]) {
  test_complex();
  std::cout << "SUCCESSFUL" << std::endl;
  return 0;
}
