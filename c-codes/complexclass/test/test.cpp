/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-04 18:57:31
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-12-11 16:31:53
 */

#include <cmath>
#include <iostream>

#include "../../codes/testplusplus.hpp"
#include "Complex.hpp"

constexpr double EPSILON = 1e-9;

bool almostEqual(double a, double b) {
  return std::abs(a - b) < EPSILON;
}

bool almostEqual(const Complex &a, const Complex &b) {
  return almostEqual(a.real, b.real) && almostEqual(a.imaginary, b.imaginary);
}

TEST(TestDefaulConstructor) {
  Complex c;
  ASSERT_EQ(c.real, 0);
  ASSERT_EQ(c.imaginary, 0);
}

TEST(TestParamConstructor) {
  Complex c(3, 4);
  ASSERT_EQ(c.real, 3);
  ASSERT_EQ(c.imaginary, 4);
}

TEST(TestFromPolar) {
  Complex c1(3, 4);
  Complex c2 = Complex::fromPolar(5, std::atan2(4, 3));
  ASSERT(almostEqual(c1, c2));
}

TEST(TestRadian) {
  Complex c(3, 4);
  ASSERT(almostEqual(c.radial(), 5));
}

TEST(TestAngular) {
  Complex c(3, 4);
  ASSERT(almostEqual(c.angular(), std::atan2(4, 3)));
}

TEST(TestConjugate) {
  Complex c(3, 4);
  Complex conj = c.conjugate();
  ASSERT_EQ(conj, Complex(3, -4));
}

TEST(TestMathOperators) {
  Complex c1(1, 2);
  Complex c2(2, -1);

  ASSERT_EQ(c1 + c2, Complex(3, 1));
  ASSERT_EQ(c1 - c2, Complex(-1, 3));
  ASSERT_EQ(c1 * c2, Complex(4, 3));
  ASSERT_EQ(c1 / c2, Complex(0, 1));
}

TEST(TestAssignOperators) {
  Complex c1(1, 2);
  Complex c2(2, -1);

  Complex c3 = c1;
  c3 += c2;
  ASSERT_EQ(c3, Complex(3, 1));

  c3 = c1;
  c3 -= c2;
  ASSERT_EQ(c1 - c2, Complex(-1, 3));

  c3 = c1;
  c3 *= c2;
  ASSERT_EQ(c1 * c2, Complex(4, 3));

  c3 = c1;
  c3 /= c2;
  ASSERT_EQ(c1 / c2, Complex(0, 1));
}

TEST(TestBinaryOperators) {
  Complex c1(1, 2), c2(1, 2), c3(2, 3);
  ASSERT(c1 == c2);
  ASSERT(c1 != c3);
  ASSERT(c1 < c3);
  ASSERT(c3 > c1);
  ASSERT(c1 <= c2);
  ASSERT(c3 >= c1);
}

TEST(TestMathFuncOperators) {
  using namespace ComplexMath;
  ASSERT_EQ(pow(Complex(0, 1), 2), Complex(-1, 0));
  ASSERT_EQ(sqrt(Complex(3, 4)), Complex(2, 1));
  ASSERT_EQ(exp(Complex(0, M_PI)), Complex(-1, 0));
  ASSERT_EQ(log(Complex(1, 0)), Complex(0, 0));
  ASSERT_EQ(sin(Complex(0, 0)), Complex(0, 0));
  ASSERT_EQ(cos(Complex(0, 0)), Complex(1, 0));
}

int main() {
  return testplusplus::runAllTests();
}
