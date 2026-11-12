#include "geometry.h"

#include <cmath>
#include <cstdio>

Point point_new(int32_t x, int32_t y) {
    Point p;
    p.x = x;
    p.y = y;
    return p;
}

double point_distance(Point a, Point b) {
    double dx = static_cast<double>(a.x - b.x);
    double dy = static_cast<double>(a.y - b.y);
    return std::sqrt(dx * dx + dy * dy);
}

int32_t add_numbers(int32_t a, int32_t b) {
    return a + b;
}

uint64_t add(uint64_t a, uint64_t b) {
    return a + b;
}

void greet(const char *name) {
    if (name == nullptr) return;
    std::printf("Hello from C++: %s\n", name);
}
