/**
 * @Author: Reza Mousavi
 * @Date:   2025-10-29 01:50:59
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2025-11-01 01:44:06
 */
#include <openssl/evp.h>
#include <openssl/rand.h>

#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

#define SHA3_256_LEN 32
#define GCM_IV_LEN 12
#define GCM_TAG_LEN 16
#define BUFFER_BLOCK_LEN 4096

std::vector<uint8_t> sha3_256(const std::string &key) {
  std::vector<uint8_t> digest(SHA3_256_LEN);
  EVP_MD_CTX *ctx = EVP_MD_CTX_new();
  EVP_DigestInit(ctx, EVP_sha3_256());
  EVP_DigestUpdate(ctx, key.data(), key.size());
  EVP_DigestFinal(ctx, digest.data(), nullptr);
  EVP_MD_CTX_free(ctx);
  return digest;
}

bool encrypt_file_gcm(const std::string &in_filename, const std::string &out_filename,
                      const std::vector<uint8_t> &key) {
  std::ifstream infile(in_filename, std::ios::binary);
  std::ofstream outfile(out_filename, std::ios::binary);
  if (!infile || !outfile) {
    return false;
  }

  std::vector<uint8_t> iv(GCM_IV_LEN), tag(GCM_TAG_LEN);
  RAND_bytes(iv.data(), iv.size());
  outfile.write(reinterpret_cast<const char *>(iv.data()), iv.size());

  EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
  EVP_EncryptInit(ctx, EVP_aes_256_gcm(), key.data(), iv.data());

  std::vector<uint8_t> inbuf(BUFFER_BLOCK_LEN);
  std::vector<uint8_t> outbuf(BUFFER_BLOCK_LEN);
  int outlen;

  while (infile.good()) {
    infile.read(reinterpret_cast<char *>(inbuf.data()), inbuf.size());
    auto bytes_read = infile.gcount();
    if (bytes_read <= 0) {
      break;
    }

    EVP_EncryptUpdate(ctx, outbuf.data(), &outlen, inbuf.data(), bytes_read);
    outfile.write(reinterpret_cast<char *>(outbuf.data()), outlen);
  }

  EVP_EncryptFinal(ctx, outbuf.data(), &outlen);
  outfile.write(reinterpret_cast<char *>(outbuf.data()), outlen);

  EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_GET_TAG, tag.size(), tag.data());
  outfile.write(reinterpret_cast<const char *>(tag.data()), tag.size());

  EVP_CIPHER_CTX_free(ctx);
  return true;
}

auto decrypt_file_gcm(const std::string &in_filename, const std::string &out_filename,
                      const std::vector<uint8_t> &key) {
  std::ifstream infile(in_filename, std::ios::binary);
  std::ofstream outfile(out_filename, std::ios::binary);
  if (!infile || !outfile) {
    return false;
  }

  infile.seekg(0, std::ios::end);
  auto totallen = infile.tellg();
  if (totallen < GCM_IV_LEN + GCM_TAG_LEN) {
    return false;
  }

  std::vector<uint8_t> iv(GCM_IV_LEN);
  infile.seekg(0, std::ios::beg);
  infile.read(reinterpret_cast<char *>(iv.data()), iv.size());

  std::vector<uint8_t> tag(GCM_TAG_LEN);
  infile.seekg(-GCM_TAG_LEN, std::ios::end);
  auto endpos = infile.tellg();
  infile.read(reinterpret_cast<char *>(tag.data()), tag.size());

  EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
  EVP_DecryptInit(ctx, EVP_aes_256_gcm(), key.data(), iv.data());

  std::vector<uint8_t> inbuf(BUFFER_BLOCK_LEN);
  std::vector<uint8_t> outbuf(BUFFER_BLOCK_LEN);
  infile.seekg(GCM_IV_LEN, std::ios::beg);
  int len = 0;
  while (infile.tellg() < endpos) {
    auto current = infile.tellg();
    std::streamsize to_read = std::min<std::streamoff>(BUFFER_BLOCK_LEN, endpos - current);
    infile.read(reinterpret_cast<char *>(inbuf.data()), to_read);
    auto read_len = infile.gcount();
    EVP_DecryptUpdate(ctx, outbuf.data(), &len, inbuf.data(), read_len);
    if (len > 0) {
      outfile.write(reinterpret_cast<char *>(outbuf.data()), len);
    }
  }

  EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_SET_TAG, tag.size(), (void *)tag.data());
  EVP_DecryptFinal(ctx, outbuf.data(), &len);
  outfile.write(reinterpret_cast<char *>(outbuf.data()), len);

  EVP_CIPHER_CTX_free(ctx);
  return true;
}

int main(int argc, char const *argv[]) {
  if (argc < 4) {
    std::cerr << "<e|d> <infile> <outfile>\n";
    return EXIT_FAILURE;
  }

  std::string method(argv[1]), infile(argv[2]), outfile(argv[3]);

  std::string input;
  std::cout << "Enter key:";
  std::getline(std::cin, input);
  auto key = sha3_256(input);
  if (key.empty()) {
    std::cout << "Error while process the key\n";
    return EXIT_FAILURE;
  }

  if (method == "e") {
    if (!encrypt_file_gcm(infile, outfile, key)) {
      std::cout << "Error while encypt file\n";
      return EXIT_FAILURE;
    }
  } else if (method == "d") {
    if (!decrypt_file_gcm(infile, outfile, key)) {
      std::cout << "Error while decypt file\n";
      return EXIT_FAILURE;
    }
  } else {
    std::cerr << "Invalid method\n";
    return EXIT_FAILURE;
  }
  return EXIT_SUCCESS;
}
