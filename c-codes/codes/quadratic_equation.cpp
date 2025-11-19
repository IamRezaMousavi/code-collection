/*
 * https://quera.org/problemset/294
 */

#include <cmath>
#include <cstdio>

int main(int argc, char const *argv[]) {
  double a, b, c;
  scanf("%lf %lf %lf", &a, &b, &c);

  if (a == 0) {
    if (b == 0) {
      if (c == 0) {
        // Not reached
      } else {
        printf("IMPOSSIBLE\n");
        return 0;
      }
    } else {
      // bx + c = 0
      double ans = -c / b;
      printf("%.3lf\n", ans);
      return 0;
    }
  }

  const double delta = b * b - 4 * a * c;
  if (delta < 0) {
    printf("IMPOSSIBLE\n");
    return 0;
  }

  const double denominator = 2 * a;
  if (delta == 0) {
    double ans = (-b) / denominator;
    printf("%.3lf\n", ans);
    return 0;
  }

  const double delta_sqrt = std::sqrt(delta);
  double ans1 = (-b + delta_sqrt) / denominator;
  double ans2 = (-b - delta_sqrt) / denominator;
  if (std::abs(ans1) < std::abs(ans2)) {
    std::swap(ans1, ans2);
  }
  printf("%.3lf\n%.3lf\n", ans1, ans2);

  return 0;
}
