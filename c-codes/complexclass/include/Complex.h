/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-04 18:51:17
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-10-28 01:17:14
 */
#ifndef __COMPLEX_H__
#define __COMPLEX_H__

#include <iostream>

class Complex {
public:
  double real, imaginary;
  Complex(const double real = 0, const double imaginary = 0);
  Complex operator()(const double real = 0, const double imaginary = 0);

  double radial() const;
  double angular() const;
  Complex conjugate() const;

  Complex operator+(const Complex other) const;
  Complex operator-(const Complex other) const;
  Complex operator*(const Complex other) const;
  Complex operator/(const Complex other) const;
  Complex operator=(const Complex other);

  Complex operator+=(const Complex other);
  Complex operator-=(const Complex other);
  Complex operator*=(const Complex other);
  Complex operator/=(const Complex other);

  bool operator==(const Complex other) const;
  bool operator!=(const Complex other) const;
  bool operator<(const Complex other) const;
  bool operator>(const Complex other) const;
  bool operator<=(const Complex other) const;
  bool operator>=(const Complex other) const;

  friend std::ostream &operator<<(std::ostream &output, const Complex &number);
  friend std::istream &operator>>(std::istream &input, Complex &number);

  friend Complex pow(const Complex base, const double power);
  friend Complex sqrt(const Complex base, const double power);
  friend Complex exp(const Complex number);
  friend Complex log(const Complex number);
  friend Complex log10(const Complex number);
  friend Complex sin(const Complex number);
  friend Complex cos(const Complex number);
  friend Complex tan(const Complex number);
  friend Complex cot(const Complex number);
  friend Complex sec(const Complex number);
  friend Complex csc(const Complex number);
  friend Complex sinh(const Complex number);
  friend Complex cosh(const Complex number);
  friend Complex tanh(const Complex number);
  friend Complex coth(const Complex number);
  friend Complex sech(const Complex number);
  friend Complex csch(const Complex number);
};

const Complex I(0, 1), J(0, 1);

Complex fromPolar(const double radial = 0, const double angular = 0);

#endif /* __COMPLEX_H__ */
