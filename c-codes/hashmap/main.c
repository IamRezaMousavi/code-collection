/**
 * @Author: Reza Mousavi
 * @Date:   2025-08-25 01:42:44
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-02 20:05:44
 */
#include <stdio.h>

#include "hashmap.h"

void print_key_value(const char *key, const char *value) {
  printf("Key: %s => Value: %s\n", key, value);
}

int main() {
  HashMap *hashmap = map_create();

  map_set(hashmap, "name", "reza");
  map_set(hashmap, "age", "24");
  map_set(hashmap, "city", "tehran");

  printf("name:   %s\n", map_get(hashmap, "name"));
  printf("age:    %s\n", map_get(hashmap, "age"));
  printf("city:   %s\n", map_get(hashmap, "city"));
  printf("home:   %s\n", map_get(hashmap, "home"));

  printf("=============\n");

  map_foreach(hashmap, print_key_value);

  printf("=============\n");

  map_delete(hashmap, "age");
  map_foreach(hashmap, print_key_value);

  map_free(hashmap);

  return 0;
}
