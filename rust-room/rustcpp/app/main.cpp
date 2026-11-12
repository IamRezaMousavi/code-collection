#include <iostream>

#include "geometry.h"

int main() {
  int sum = add_numbers(10, 32) + add(50, 22);
  std::cout << "sum is = " << sum << std::endl;

  Point s{.x = 0, .y = 0};

  Point p = point_new(3, 4);
  double dist = point_distance(p, s);
  std::cout << "dist point from start = " << dist << std::endl;

  greet("World C++");

  return 0;
}
