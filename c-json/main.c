#include <stdio.h>
#include <string.h>

#include "cJSON.h"

int main() {
  cJSON *object = cJSON_CreateObject();
  cJSON_AddStringToObject(object, "name", "Reza");
  cJSON_AddNumberToObject(object, "height", 20);

  char *string = cJSON_PrintUnformatted(object);
  printf("Object: %s, %d\n", string, strlen(string));
  cJSON_Delete(object);

  cJSON *object2 = cJSON_Parse("{\"name\":\"Reza\",\"height\":20}");
  cJSON *name2 = cJSON_GetObjectItem(object2, "name");
  cJSON *height2 = cJSON_GetObjectItem(object2, "height");

  printf(
	  "Name: %s, Height: %d\n", name2->valuestring, (int)height2->valuedouble);

  cJSON_Delete(object2);

  return 0;
}
