/**
 * @Author: Reza Mousavi
 * @Date:   2025-08-25 01:42:49
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-02 20:02:09
 */
#ifndef __HASHMAP_H__
#define __HASHMAP_H__

#define HASHMAP_SIZE 101

typedef struct Node {
  char *key;
  char *value;
  struct Node *next;
} Node;

typedef struct HashMap {
  Node *buckets[HASHMAP_SIZE];
} HashMap;

HashMap *map_create();
void map_set(HashMap *hashmap, const char *key, const char *value);
char *map_get(HashMap *hashmap, const char *key);
void map_delete(HashMap *hashmap, const char *key);
void map_foreach(HashMap *hashmap, void (*callback)(const char *, const char *));
void map_free(HashMap *hashmap);

#endif /* __HASHMAP_H__ */
