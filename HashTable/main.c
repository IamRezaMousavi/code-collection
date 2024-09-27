#include <glib.h>

int main() {
  GHashTable *hash_table = g_hash_table_new(g_str_hash, g_str_equal);

  g_hash_table_insert(hash_table, "name", "Reza");
  g_hash_table_insert(hash_table, "city", "Tehran");

  gchar *name = g_hash_table_lookup(hash_table, "name");
  gchar *city = g_hash_table_lookup(hash_table, "city");

  g_print("Name: %s\n", name);
  g_print("City: %s\n", city);

  if (!g_hash_table_contains(hash_table, "age")) g_print("Age not found\n");

  g_hash_table_destroy(hash_table);

  return 0;
}
