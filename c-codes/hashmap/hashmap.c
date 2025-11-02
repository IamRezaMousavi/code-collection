/**
 * @Author: Reza Mousavi
 * @Date:   2025-08-25 01:42:44
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-02 20:23:22
 */
#include "hashmap.h"

#include <stdint.h>
#include <stdlib.h>
#include <string.h>

// MurmurHash3
static uint32_t murmurhash(const char *key, uint32_t len, uint32_t seed) {
  const uint32_t c1 = 0xcc9e2d51;
  const uint32_t c2 = 0x1b873593;
  const uint32_t r1 = 15;
  const uint32_t r2 = 13;
  const uint32_t m = 5;
  const uint32_t n = 0xe6546b64;

  uint32_t hash = seed;
  const int nblocks = len / 4;
  const uint32_t *blocks = (const uint32_t *)(key);
  for (int i = 0; i < nblocks; i++) {
    uint32_t k = blocks[i];
    k *= c1;
    k = (k << r1) | (k >> (32 - r1));
    k *= c2;

    hash ^= k;
    hash = (hash << r2) | (hash >> (32 - r2));
    hash = hash * m + n;
  }

  const uint8_t *tail = (const uint8_t *)(key + nblocks * 4);
  uint32_t k1 = 0;

  switch (len & 3) {
  case 3:
    k1 ^= tail[2] << 16;
  case 2:
    k1 ^= tail[1] << 8;
  case 1:
    k1 ^= tail[0];
    k1 *= c1;
    k1 = (k1 << r1) | (k1 >> (32 - r1));
    k1 *= c2;
    hash ^= k1;
  }

  hash ^= len;
  hash ^= (hash >> 16);
  hash *= 0x85ebca6b;
  hash ^= (hash >> 13);
  hash *= 0xc2b2ae35;
  hash ^= (hash >> 16);

  return hash;
}

static Node *node_create(const char *key, const char *value) {
  Node *new_node = (Node *)malloc(sizeof(Node));
  new_node->key = strdup(key);
  new_node->value = strdup(value);
  new_node->next = NULL;
  return new_node;
}

static void node_free(Node *node) {
  free(node->key);
  free(node->value);
  free(node);
}

HashMap *map_create() {
  HashMap *hashmap = (HashMap *)malloc(sizeof(HashMap));
  for (int i = 0; i < HASHMAP_SIZE; i++)
    hashmap->buckets[i] = NULL;
  return hashmap;
}

void map_set(HashMap *hashmap, const char *key, const char *value) {
  uint32_t hash = murmurhash(key, strlen(key), 0);
  int index = hash % HASHMAP_SIZE;

  Node *current = hashmap->buckets[index];
  while (current) {
    if (strcmp(current->key, key) == 0) {
      // update value
      free(current->value);
      current->value = strdup(value);
      return;
    }
    current = current->next;
  }

  Node *new_node = node_create(key, value);
  new_node->next = hashmap->buckets[index];
  hashmap->buckets[index] = new_node;
}

char *map_get(HashMap *hashmap, const char *key) {
  uint32_t hash = murmurhash(key, strlen(key), 0);
  int index = hash % HASHMAP_SIZE;

  Node *current = hashmap->buckets[index];
  while (current) {
    if (strcmp(current->key, key) == 0)
      return current->value;
    current = current->next;
  }
  return NULL;
}

void map_delete(HashMap *hashmap, const char *key) {
  uint32_t hash = murmurhash(key, strlen(key), 0);
  int index = hash % HASHMAP_SIZE;

  Node *current = hashmap->buckets[index];
  Node *prev = NULL;
  while (current) {
    if (strcmp(current->key, key) == 0) {
      if (prev) {
        prev->next = current->next;
      } else {
        hashmap->buckets[index] = current->next;
      }

      node_free(current);
      return;
    }

    prev = current;
    current = current->next;
  }
}

void map_foreach(HashMap *hashmap, void (*callback)(const char *, const char *)) {
  for (int i = 0; i < HASHMAP_SIZE; i++) {
    Node *current = hashmap->buckets[i];
    while (current) {
      callback(current->key, current->value);
      current = current->next;
    }
  }
}

void map_free(HashMap *hashmap) {
  for (int i = 0; i < HASHMAP_SIZE; i++) {
    Node *current = hashmap->buckets[i];
    while (current) {
      Node *temp = current;
      current = current->next;
      node_free(temp);
    }
  }
  free(hashmap);
}
