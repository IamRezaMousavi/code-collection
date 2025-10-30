#include <cjson/cJSON.h>
#include <curl/curl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct MemoryStruct {
  char *memory;
  size_t size;
};

static size_t WriteMemoryCallback(void *contents, size_t size, size_t nmemb, void *userp) {
  size_t realsize = size * nmemb;
  struct MemoryStruct *mem = (struct MemoryStruct *)userp;

  char *ptr = realloc(mem->memory, mem->size + realsize + 1);
  if (ptr == NULL) {
    printf("Not enough memory (realloc returned NULL)\n");
    return 0;
  }

  mem->memory = ptr;
  memcpy(&(mem->memory[mem->size]), contents, realsize);
  mem->size += realsize;
  mem->memory[mem->size] = 0;

  return realsize;
}

char *http_get(const char *url) {
  CURL *curl_handle;
  CURLcode res;

  struct MemoryStruct chunk;
  chunk.memory = malloc(1);
  chunk.size = 0;

  curl_global_init(CURL_GLOBAL_DEFAULT);
  curl_handle = curl_easy_init();
  if (curl_handle) {
    curl_easy_setopt(curl_handle, CURLOPT_URL, url);
    curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
    curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, (void *)&chunk);

    res = curl_easy_perform(curl_handle);
    if (res != CURLE_OK) {
      fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
      free(chunk.memory);
      chunk.memory = NULL;
    }

    curl_easy_cleanup(curl_handle);
  }
  curl_global_cleanup();

  return chunk.memory;
}

int main() {
  const char *cityname = "London";
  const char *API_KEY = "58339b029b4279319dfd339d5f21d532";
  char url[512];
  snprintf(url, sizeof(url), "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s", cityname, API_KEY);

  char *response = http_get(url);
  if (response == NULL) {
    printf("Failed to get response\n");
    return 1;
  }

  cJSON *json = cJSON_Parse(response);
  if (json == NULL) {
    printf("Error parsing JSON\n");
    free(response);
    return 1;
  }

  cJSON *main_obj = cJSON_GetObjectItemCaseSensitive(json, "main");
  if (cJSON_IsObject(main_obj)) {
    cJSON *temp_obj = cJSON_GetObjectItemCaseSensitive(main_obj, "temp");
    if (cJSON_IsNumber(temp_obj)) {
      printf("Temp is: %f\n", temp_obj->valuedouble);
    } else {
      printf("Temp not found!\n");
    }
  } else {
    printf("Main object not found!\n");
  }

  cJSON_Delete(json);
  free(response);
  return 0;
}
