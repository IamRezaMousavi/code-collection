/**
 * @Author: @IamRezaMousavi
 * @Date:   2021-12-04 18:54:41
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-02 22:08:53
 */

#include "Complex.hpp"

#include <cmath>
#include <iostream>

Complex::Complex(const double real, const double imaginary) {
  this->real = real;
  this->imaginary = imaginary;
}

Complex Complex::fromPolar(const double radial, const double angular) {
  double real = radial * std::cos(angular), imaginary = radial * std::sin(angular);
  real = std::round(real * 100000) / 100000;
  imaginary = std::round(imaginary * 100000) / 100000;
  return Complex(real, imaginary);
}

// -----------------------
double Complex::radial() const {
  return sqrt(pow(real, 2) + pow(imaginary, 2));
}

double Complex::angular() const {
  return atan(imaginary / real);
}

Complex Complex::conjugate() const {
  return Complex(real, -imaginary);
}

// -----------------------
Complex Complex::operator+(const Complex &other) const {
  return Complex(real + other.real, imaginary + other.imaginary);
}

Complex Complex::operator-(const Complex &other) const {
  return Complex(real - other.real, imaginary - other.imaginary);
}

Complex Complex::operator*(const Complex &other) const {
  double realPart = real * other.real - imaginary * other.imaginary,
         imaginaryPart = real * other.imaginary + imaginary * other.real;
  return Complex(realPart, imaginaryPart);
}

Complex Complex::operator/(const Complex &other) const {
  double denominator = other.real * other.real + other.imaginary * other.imaginary;
  double realNumerator = real * other.real + imaginary * other.imaginary;
  double imaginaryNumerator = imaginary * other.real - real * other.imaginary;
  return Complex(realNumerator / denominator, imaginaryNumerator / denominator);
}

// ----------------------
Complex Complex::operator+=(const Complex &other) {
  real = real + other.real;
  imaginary = imaginary + other.imaginary;
  return *this;
}

Complex Complex::operator-=(const Complex &other) {
  real = real - other.real;
  imaginary = imaginary - other.imaginary;
  return *this;
}

Complex Complex::operator*=(const Complex &other) {
  real = real * other.real - imaginary * other.imaginary;
  imaginary = real * other.imaginary + imaginary * other.real;
  return *this;
}

Complex Complex::operator/=(const Complex &other) {
  double denominator = other.real * other.real + other.imaginary * other.imaginary;
  double realNumerator = real * other.real + imaginary * other.imaginary;
  double imaginaryNumerator = imaginary * other.real - real * other.imaginary;

  real = realNumerator / denominator;
  imaginary = imaginaryNumerator / denominator;
  return *this;
}

// ---------------------------
bool Complex::operator==(const Complex &other) const {
  return (real == other.real) && (imaginary == other.imaginary);
}

bool Complex::operator!=(const Complex &other) const {
  return !((real == other.real) && (imaginary == other.imaginary));
}

bool Complex::operator<(const Complex &other) const {
  return (real < other.real) ? true : ((real == other.real && imaginary < other.imaginary) ? true : false);
}

bool Complex::operator>(const Complex &other) const {
  return (real > other.real) ? true : ((real == other.real && imaginary > other.imaginary) ? true : false);
}

bool Complex::operator<=(const Complex &other) const {
  return (real <= other.real) ? true : ((real == other.real && imaginary <= other.imaginary) ? true : false);
}

bool Complex::operator>=(const Complex &other) const {
  return (real >= other.real) ? true : ((real == other.real && imaginary >= other.imaginary) ? true : false);
}

// ---------------------------
std::ostream &operator<<(std::ostream &output, const Complex &number) {
  // for complex(0, 0)
  if (number.real == 0 && number.imaginary == 0) {
    output << std::noshowpos << 0;
    return output;
  }
  // for complex(real)
  if (number.real != 0 && number.imaginary == 0) {
    output << std::noshowpos << number.real;
    return output;
  }
  // for complex(0, imaginary)
  if (number.real == 0 && number.imaginary != 0) {
    if (number.imaginary == 1)
      output << "i";
    else if (number.imaginary == -1)
      output << "-i";
    else
      output << std::noshowpos << number.imaginary << "i";
    return output;
  }
  // for complex(real, imaginary)
  // complex(real, 1)
  if (number.imaginary == 1) {
    output << std::noshowpos << number.real << std::noshowpoint << "+i";
  } else if (number.imaginary == -1) {
    // complex(real, -1)
    output << std::noshowpos << number.real << std::noshowpoint << "-i";
  } else {
    output << std::noshowpos << number.real << std::showpos << number.imaginary << std::noshowpoint << "i"
           << std::noshowpos;
  }
  return output;
}

std::istream &operator>>(std::istream &input, Complex &number) {
  input >> number.real >> number.imaginary;
  return input;
}

namespace ComplexMath {

Complex pow(const Complex base, const double power) {
  double radial = std::pow(base.radial(), power), angular = base.angular() * power;
  return Complex::fromPolar(radial, angular);
}

Complex sqrt(const Complex base, const double power = 2) {
  return pow(base, 1 / power);
}

Complex exp(const Complex number) {
  return Complex::fromPolar(std::exp(number.real), number.imaginary);
}

Complex log(const Complex number) {
  return Complex(std::log(number.radial()), number.angular());
}

Complex log10(const Complex number) {
  return log(number) / (Complex)log(10);
}

Complex sin(const Complex number) {
  double real = std::sin(number.real) * std::cosh(number.imaginary),
         imaginary = std::cos(number.real) * std::sinh(number.imaginary);
  return Complex(real, imaginary);
}

Complex cos(const Complex number) {
  double real = std::cos(number.real) * std::cosh(number.imaginary),
         imaginary = -std::sin(number.real) * std::sinh(number.imaginary);
  return Complex(real, imaginary);
}

Complex tan(const Complex number) {
  return sin(number) / cos(number);
}

Complex cot(const Complex number) {
  return cos(number) / sin(number);
}

Complex sec(const Complex number) {
  return (Complex)1 / cos(number);
}

Complex csc(const Complex number) {
  return (Complex)1 / sin(number);
}

Complex sinh(const Complex number) {
  return (exp(number) - exp((Complex)-1 * number)) / 2;
}

Complex cosh(const Complex number) {
  return (exp(number) + exp((Complex)-1 * number)) / 2;
}

Complex tanh(const Complex number) {
  return sinh(number) / cosh(number);
}

Complex coth(const Complex number) {
  return cosh(number) / sinh(number);
}

Complex sech(const Complex number) {
  return (Complex)1 / cosh(number);
}

Complex csch(const Complex number) {
  return (Complex)1 / sinh(number);
}

} // namespace ComplexMath
