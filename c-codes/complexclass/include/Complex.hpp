/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-04 18:51:17
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-02 22:09:57
 */
#ifndef __COMPLEX_HPP__
#define __COMPLEX_HPP__

#include <iostream>

class Complex {
public:
  double real, imaginary;

  Complex() = default;
  Complex(const double real = 0, const double imaginary = 0);
  static Complex fromPolar(const double radial = 0, const double angular = 0);

  Complex(const Complex &) = default;
  Complex(Complex &&) = default;
  Complex &operator=(Complex &&) = default;
  Complex &operator=(const Complex &) = default;

  ~Complex() = default;

  double radial() const;
  double angular() const;
  Complex conjugate() const;

  Complex operator+(const Complex &other) const;
  Complex operator-(const Complex &other) const;
  Complex operator*(const Complex &other) const;
  Complex operator/(const Complex &other) const;

  Complex operator+=(const Complex &other);
  Complex operator-=(const Complex &other);
  Complex operator*=(const Complex &other);
  Complex operator/=(const Complex &other);

  bool operator==(const Complex &other) const;
  bool operator!=(const Complex &other) const;
  bool operator<(const Complex &other) const;
  bool operator>(const Complex &other) const;
  bool operator<=(const Complex &other) const;
  bool operator>=(const Complex &other) const;

  friend std::ostream &operator<<(std::ostream &output, const Complex &number);
  friend std::istream &operator>>(std::istream &input, Complex &number);
};

namespace ComplexMath {

Complex pow(const Complex base, const double power);
Complex sqrt(const Complex base, const double power);
Complex exp(const Complex number);
Complex log(const Complex number);
Complex log10(const Complex number);
Complex sin(const Complex number);
Complex cos(const Complex number);
Complex tan(const Complex number);
Complex cot(const Complex number);
Complex sec(const Complex number);
Complex csc(const Complex number);
Complex sinh(const Complex number);
Complex cosh(const Complex number);
Complex tanh(const Complex number);
Complex coth(const Complex number);
Complex sech(const Complex number);
Complex csch(const Complex number);

} // namespace ComplexMath

const Complex I(0, 1), J(0, 1);

#endif /* __COMPLEX_HPP__ */
