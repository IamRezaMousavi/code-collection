/**
 * @Author: Reza Mousavi
 * @Date:   2025-08-25 01:42:44
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2026-01-23 18:58:35
 */
#include "hashmap.h"

#include <stdint.h>
#include <string.h>

#define MMH_SEED 0x9747b28c

static inline uint32_t rotl32(uint32_t x, uint32_t r) {
  return (x << r) | (x >> (32 - r));
}

static inline uint32_t fmix32(uint32_t h) {
  h ^= h >> 16;
  h *= 0x85ebca6b;
  h ^= (h >> 13);
  h *= 0xc2b2ae35;
  h ^= (h >> 16);
  return h;
}

// MurmurHash3_x86_32
static uint32_t murmurhash(const char *key, size_t len, uint32_t seed) {
  const uint32_t c1 = 0xcc9e2d51;
  const uint32_t c2 = 0x1b873593;
  const uint32_t r1 = 15;
  const uint32_t r2 = 13;
  const uint32_t m = 5;
  const uint32_t n = 0xe6546b64;

  const uint8_t *data = (const uint8_t *)key;
  const size_t nblocks = len / 4;
  uint32_t hash = seed;

  //----------
  // body
  const uint32_t *blocks = (const uint32_t *)(data + nblocks * 4);
  for (size_t i = -nblocks; i; i++) {
    uint32_t k1 = blocks[i];

    k1 *= c1;
    k1 = rotl32(k1, r1);
    k1 *= c2;

    hash ^= k1;
    hash = rotl32(hash, r2);
    hash = hash * m + n;
  }

  //----------
  // tail
  const uint8_t *tail = (const uint8_t *)(data + nblocks * 4);
  uint32_t k1 = 0;
  switch (len & 3) {
  case 3:
    k1 ^= tail[2] << 16;
  case 2:
    k1 ^= tail[1] << 8;
  case 1:
    k1 ^= tail[0];
    k1 *= c1;
    k1 = rotl32(k1, r1);
    k1 *= c2;
    hash ^= k1;
  };

  //----------
  // finalization
  hash ^= len;
  hash = fmix32(hash);
  return hash;
}

void map_init(HashMap *hashmap) {
  for (int i = 0; i < HASHMAP_SIZE; i++) {
    hashmap->buckets[i].count = 0;
  }
}

bool map_set(HashMap *hashmap, const char *key, const char *value) {
  uint32_t hash = murmurhash(key, strlen(key), MMH_SEED);
  uint32_t index = hash % HASHMAP_SIZE;

  Bucket *bucket = &hashmap->buckets[index];

  // update if key exists
  for (size_t i = 0; i < bucket->count; i++) {
    if (bucket->nodes[i].hash == hash && strcmp(bucket->nodes[i].key, key) == 0) {

      strncpy(bucket->nodes[i].value, value, MAX_VALUE_LEN - 1);
      bucket->nodes[i].value[MAX_VALUE_LEN - 1] = '\0';
      return true;
    }
  }

  // no space
  if (bucket->count >= BUCKET_CAPACITY)
    return false;

  // insert
  Node *node = &bucket->nodes[bucket->count++];
  node->hash = hash;

  strncpy(node->key, key, MAX_KEY_LEN - 1);
  node->key[MAX_KEY_LEN - 1] = '\0';

  strncpy(node->value, value, MAX_VALUE_LEN - 1);
  node->value[MAX_VALUE_LEN - 1] = '\0';

  node->hash = hash;

  return true;
}

const char *map_get(const HashMap *hashmap, const char *key) {
  uint32_t hash = murmurhash(key, strlen(key), MMH_SEED);
  uint32_t index = hash % HASHMAP_SIZE;

  const Bucket *bucket = &hashmap->buckets[index];

  for (size_t i = 0; i < bucket->count; i++) {
    if (bucket->nodes[i].hash == hash && strcmp(bucket->nodes[i].key, key) == 0) {
      return bucket->nodes[i].value;
    }
  }
  return NULL;
}

bool map_delete(HashMap *hashmap, const char *key) {
  uint32_t hash = murmurhash(key, strlen(key), MMH_SEED);
  uint32_t index = hash % HASHMAP_SIZE;

  Bucket *bucket = &hashmap->buckets[index];

  for (size_t i = 0; i < bucket->count; i++) {
    if (bucket->nodes[i].hash == hash && strcmp(bucket->nodes[i].key, key) == 0) {

      // shift left
      for (size_t j = i + 1; j < bucket->count; j++) {
        bucket->nodes[j - 1] = bucket->nodes[j];
      }
      bucket->count--;
      return true;
    }
  }
  return false;
}

void map_foreach(const HashMap *hashmap, void (*callback)(const char *, const char *)) {
  for (int i = 0; i < HASHMAP_SIZE; i++) {
    const Bucket *bucket = &hashmap->buckets[i];
    for (size_t j = 0; j < bucket->count; j++) {
      callback(bucket->nodes[j].key, bucket->nodes[j].value);
    }
  }
}

void map_clear(HashMap *hashmap) {
  for (int i = 0; i < HASHMAP_SIZE; i++)
    hashmap->buckets[i].count = 0;
}
