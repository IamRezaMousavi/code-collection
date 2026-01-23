/**
 * @Author: Reza Mousavi
 * @Date:   2025-08-25 01:42:49
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2026-01-23 18:54:08
 */
#ifndef __HASHMAP_H__
#define __HASHMAP_H__

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#define HASHMAP_SIZE 101
#define BUCKET_CAPACITY 10
#define MAX_KEY_LEN 32
#define MAX_VALUE_LEN 64

typedef struct Node {
  char key[MAX_KEY_LEN];
  char value[MAX_VALUE_LEN];
  uint32_t hash;
} Node;

typedef struct Bucket {
  Node nodes[BUCKET_CAPACITY];
  size_t count;
} Bucket;

typedef struct HashMap {
  Bucket buckets[HASHMAP_SIZE];
} HashMap;

void map_init(HashMap *hashmap);
bool map_set(HashMap *hashmap, const char *key, const char *value);
const char *map_get(const HashMap *hashmap, const char *key);
bool map_delete(HashMap *hashmap, const char *key);
void map_foreach(const HashMap *hashmap, void (*callback)(const char *, const char *));
void map_clear(HashMap *hashmap);

#endif /* __HASHMAP_H__ */
