/*
 * https://quera.org/problemset/593
 */

#include <cmath>
#include <iostream>

bool is_prime(int num) {
  if (num < 2)
    return false;
  if (num == 2)
    return true;
  if (num % 2 == 0)
    return false;
  int limit = static_cast<int>(std::sqrt(num));
  for (int i = 3; i <= limit; i += 2)
    if (num % i == 0)
      return false;
  return true;
}

int main(int argc, char const *argv[]) {
  int number;
  std::cin >> number;

  int n = number;
  int sum = 0;
  while (n > 0) {
    sum += n % 10;
    n /= 10;
  }

  int counter = 0;
  int result = 0;
  for (int i = number + 1; counter < sum; i++) {
    if (is_prime(i)) {
      counter++;
      result = i;
    }
  }

  std::cout << result << '\n';

  return 0;
}
