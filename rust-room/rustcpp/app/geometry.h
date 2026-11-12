#pragma once

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

typedef struct Point {
  int32_t x;
  int32_t y;
} Point;

Point point_new(int32_t x, int32_t y);
double point_distance(Point a, Point b);

int32_t add_numbers(int32_t a, int32_t b);
uint64_t add(uint64_t a, uint64_t b);

void greet(const char *name);

#ifdef __cplusplus
}
#endif
