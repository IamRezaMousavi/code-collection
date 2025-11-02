/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-04 18:57:31
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-03 00:29:10
 */

#include <cmath>
#include <iostream>

#include "Complex.hpp"

#define COLOR_RESET "\033[0m"
#define COLOR_GREEN "\033[32m"
#define COLOR_RED "\033[31m"
#define COLOR_YELLOW "\033[33m"
#define COLOR_CYAN "\033[36m"
#define COLOR_BOLD "\033[1m"

constexpr double EPSILON = 1e-9;

static int total_tests = 0;
static int passed_tests = 0;

bool almostEqual(double a, double b) {
  return std::abs(a - b) < EPSILON;
}

bool almostEqual(const Complex &a, const Complex &b) {
  return almostEqual(a.real, b.real) && almostEqual(a.imaginary, b.imaginary);
}

#define TEST_EQ(name, result, expected)                                                                                \
  do {                                                                                                                 \
    ++total_tests;                                                                                                     \
    auto _res = (result);                                                                                              \
    auto _exp = (expected);                                                                                            \
    bool ok = almostEqual(_res, _exp);                                                                                 \
    if (ok) {                                                                                                          \
      ++passed_tests;                                                                                                  \
      std::cout << COLOR_GREEN << "[OK]  " << COLOR_RESET << name << std::endl;                                        \
    } else {                                                                                                           \
      std::cout << COLOR_RED << "[ERR] " << name << COLOR_RESET << " | got (" << _res.real << ", " << _res.imaginary   \
                << ")"                                                                                                 \
                << " | expected (" << _exp.real << ", " << _exp.imaginary << ")" << std::endl;                         \
    }                                                                                                                  \
  } while (0)

#define TEST_BOOL(name, expr)                                                                                          \
  do {                                                                                                                 \
    ++total_tests;                                                                                                     \
    bool ok = (expr);                                                                                                  \
    if (ok) {                                                                                                          \
      ++passed_tests;                                                                                                  \
      std::cout << COLOR_GREEN << "[OK]  " << COLOR_RESET << name << std::endl;                                        \
    } else {                                                                                                           \
      std::cout << COLOR_RED << "[ERR] " << name << COLOR_RESET << std::endl;                                          \
    }                                                                                                                  \
  } while (0)

void test_complex() {
  Complex c1;
  TEST_BOOL("default constructor", c1.real == 0 && c1.imaginary == 0);

  Complex c2(3, 4);
  TEST_BOOL("param constructor", c2.real == 3 && c2.imaginary == 4);

  Complex c3 = Complex::fromPolar(5, std::atan2(4, 3));
  TEST_EQ("fromPolar()", c3, c2);

  TEST_BOOL("radial()", almostEqual(c2.radial(), 5));
  TEST_BOOL("angular()", almostEqual(c2.angular(), std::atan2(4, 3)));

  Complex conj = c2.conjugate();
  TEST_EQ("conjugate()", conj, Complex(3, -4));

  Complex c4(1, 2);
  Complex c5(2, -1);

  TEST_EQ("operator+", c4 + c5, Complex(3, 1));
  TEST_EQ("operator-", c4 - c5, Complex(-1, 3));
  TEST_EQ("operator*", c4 * c5, Complex(4, 3));
  TEST_EQ("operator/", c4 / c5, Complex(0, 1));

  Complex c6 = c4;
  c6 += c5;
  TEST_EQ("operator+=", c6, Complex(3, 1));

  c6 = c4;
  c6 -= c5;
  TEST_EQ("operator-=", c6, Complex(-1, 3));

  c6 = c4;
  c6 *= c5;
  TEST_EQ("operator*=", c6, Complex(4, 3));

  c6 = c4;
  c6 /= c5;
  TEST_EQ("operator/=", c6, Complex(0, 1));

  Complex c7(1, 2), c8(1, 2), c9(2, 3);
  TEST_BOOL("==", c7 == c8);
  TEST_BOOL("!=", c7 != c9);
  TEST_BOOL("<", c7 < c9);
  TEST_BOOL(">", c9 > c7);
  TEST_BOOL("<=", c7 <= c8);
  TEST_BOOL(">=", c9 >= c7);

  using namespace ComplexMath;
  TEST_EQ("pow()", pow(Complex(0, 1), 2), Complex(-1, 0));
  TEST_EQ("sqrt()", sqrt(Complex(3, 4)), Complex(2, 1));
  TEST_EQ("exp()", exp(Complex(0, M_PI)), Complex(-1, 0));
  TEST_EQ("log()", log(Complex(1, 0)), Complex(0, 0));
  TEST_EQ("sin()", sin(Complex(0, 0)), Complex(0, 0));
  TEST_EQ("cos()", cos(Complex(0, 0)), Complex(1, 0));
}

int main() {
  test_complex();

  int failed = total_tests - passed_tests;
  double rate = 100.0 * passed_tests / total_tests;

  std::cout << "\n" << COLOR_YELLOW << "───────────────── SUMMARY ────────────────" << COLOR_RESET << "\n";
  std::cout << COLOR_CYAN << "Total: " << total_tests << " | Passed: " << COLOR_GREEN << passed_tests << COLOR_CYAN
            << " | Failed: " << (failed ? COLOR_RED : COLOR_GREEN) << failed << COLOR_CYAN
            << " | Success rate: " << COLOR_BOLD << rate << "%" << COLOR_RESET << std::endl;
  std::cout << COLOR_YELLOW << "──────────────────────────────────────────" << COLOR_RESET << "\n";

  return (failed == 0) ? 0 : 1;
}
