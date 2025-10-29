/**
 * @Author: Reza Mousavi
 * @Date:   2025-10-29 01:50:59
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-10-29 02:12:14
 */
#include <openssl/evp.h>

#include <iomanip>
#include <iostream>
#include <string>

int main(int argc, char const *argv[]) {
  std::string input;
  std::cout << "Enter text:";
  std::getline(std::cin, input);

  EVP_MD_CTX *ctx = EVP_MD_CTX_new();
  if (!ctx) {
    std::cerr << "Error: failed to create EVP context.\n";
    return EXIT_FAILURE;
  }

  if (EVP_DigestInit(ctx, EVP_sha3_512()) != 1) {
    std::cerr << "Error: EVP_DigestInit failed.\n";
    EVP_MD_CTX_free(ctx);
    return EXIT_FAILURE;
  }

  if (EVP_DigestUpdate(ctx, input.data(), input.size()) != 1) {
    std::cerr << "Error: EVP_DigestUpdate failed.\n";
    EVP_MD_CTX_free(ctx);
    return EXIT_FAILURE;
  }

  unsigned char hash[EVP_MAX_MD_SIZE];
  unsigned int hash_len = 0;
  if (EVP_DigestFinal(ctx, hash, &hash_len) != 1) {
    std::cerr << "Error: EVP_DigestFinal failed.\n";
    EVP_MD_CTX_free(ctx);
    return EXIT_FAILURE;
  }

  EVP_MD_CTX_free(ctx);

  std::cout << "SHA3-512: ";
  for (unsigned int i = 0; i < hash_len; i++) {
    std::cout << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(hash[i]);
  }
  std::cout << std::dec << std::endl;

  return EXIT_SUCCESS;
}
