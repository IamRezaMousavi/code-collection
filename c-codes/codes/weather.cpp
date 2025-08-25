#include <curl/curl.h>
#include <nlohmann/json.hpp>

#include <iostream>

static size_t WriteCallback(void *contents, size_t size, size_t nmemb,
                            void *userp) {
  ((std::string *)userp)->append((char *)contents, size * nmemb);
  return size * nmemb;
}

std::string http_get(const std::string &url) {
  CURL *curl;
  CURLcode res;
  std::string readBuffer;

  curl_global_init(CURL_GLOBAL_DEFAULT);
  curl = curl_easy_init();
  if (curl) {
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

    res = curl_easy_perform(curl);
    if (res != CURLE_OK) {
      std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res)
                << std::endl;
      readBuffer = ""; // if got error, return empty string
    }
    curl_easy_cleanup(curl);
  }
  curl_global_cleanup();

  return readBuffer;
}

int main(int argc, char const *argv[]) {
  std::string url_base = "http://api.openweathermap.org/data/2.5/weather?q=";
  std::string cityname = "London";
  std::string API_KEY = "58339b029b4279319dfd339d5f21d532";
  std::string url = url_base + cityname + "&appid=" + API_KEY; // + "&lang=fa"
  std::string response = http_get(url);

  auto data = nlohmann::json::parse(response);
  std::cout << data.dump(2) << std::endl;

  if (data.contains("main") && data["main"].contains("temp")) {
    double temp = data["main"]["temp"].get<double>();
    std::cout << "Temp is " << temp << std::endl;
  } else {
    std::cerr << "Temp not found!" << std::endl;
  }
  return 0;
}
