#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/miller_rabin.hpp>
#include <boost/random.hpp>

#include <cstdint>
#include <iostream>
#include <optional>
#include <vector>

using BigInt = boost::multiprecision::cpp_int;
using Bytes = std::vector<uint8_t>;

/**
 * r = base^exp mod mod
 */
BigInt pow_mod(BigInt base, BigInt exp, const BigInt &mod) {
  BigInt result = 1;
  base %= mod;
  while (exp > 0) {
    if (exp & 1)
      result = (result * base) % mod;
    base = (base * base) % mod;
    exp >>= 1;
  }
  return result;
}

/**
 * Extended GCD
 * ax + by = gcd(a, b)
 */
BigInt egcd(const BigInt &a, const BigInt &b, BigInt &x, BigInt &y) {
  if (b == 0) {
    x = 1;
    y = 0;
    return a;
  }
  BigInt x1, y1;
  BigInt g = egcd(b, a % b, x1, y1);
  x = y1;
  y = x1 - (a / b) * y1;
  return g;
}

/**
 * ax ≡ 1 (mod m)
 * or
 * x ≡ a^(-1) (mod m)
 */
BigInt mod_inverse(const BigInt &a, const BigInt &mod) {
  BigInt x, y;
  if (egcd(a, mod, x, y) != 1)
    throw std::runtime_error("No inverse");
  x %= mod;
  return x < 0 ? x + mod : x;
}

bool is_prime(const BigInt &n) {
  if (n < 2)
    return false;
  boost::random::mt19937 gen(std::random_device{}());
  return boost::multiprecision::miller_rabin_test(n, 25, gen);
}

/**
 * Generates a random odd integer having exactly `bits` bits.
 */
BigInt random_bigint(int bits) {
  static boost::random::mt19937 gen(std::random_device{}());
  boost::random::uniform_int_distribution<uint64_t> dist(0, UINT64_MAX);

  BigInt value = 0;
  for (int i = 0; i < bits; i += 64)
    value = (value << 64) | dist(gen);

  value |= BigInt(1) << (bits - 1); // ensure bit length
  value |= 1;                       // make odd
  return value;
}

BigInt random_prime(int bits) {
  while (true) {
    BigInt x = random_bigint(bits);
    if (is_prime(x))
      return x;
  }
}

size_t bytes_count(const BigInt &n) {
  BigInt value = n;
  size_t bits = 0;
  while (value > 0) {
    value >>= 1;
    bits++;
  }
  return (bits + 7) / 8;
}

Bytes bigint_to_bytes(const BigInt &value) {
  if (value == 0)
    return {0};

  BigInt n = value;
  Bytes bytes;

  while (n > 0) {
    bytes.push_back(static_cast<uint8_t>(n & 0xFF));
    n >>= 8;
  }

  std::reverse(bytes.begin(), bytes.end());
  return bytes;
}

BigInt bytes_to_bigint(const Bytes &bytes) {
  BigInt value = 0;
  for (uint8_t byte : bytes) {
    value <<= 8;
    value += byte;
  }
  return value;
}

Bytes bigint_to_bytes_fixed(const BigInt &value, size_t size) {
  Bytes bytes(size, 0);
  BigInt n = value;

  for (size_t i = 0; i < size; i++) {
    bytes[size - 1 - i] = static_cast<uint8_t>(n & 0xFF);
    n >>= 8;
  }
  return bytes;
}

std::optional<BigInt> integer_root(const BigInt &value, const BigInt &e) {
  // Binary search for integer e-th root
  BigInt lo = 0;
  BigInt hi = value;
  while (lo <= hi) {
    BigInt mid = (lo + hi) / 2;

    // Compute mid^e
    BigInt power = 1;
    for (BigInt i = 0; i < e; ++i)
      power *= mid;

    if (power == value)
      return mid;

    if (power < value)
      lo = mid + 1;
    else
      hi = mid - 1;
  }

  return std::nullopt;
}

/**
 * Low exponent attack (generalized)
 * If m^e < n, then c = m^e,
 * and m can be recovered by taking the integer e-th root of c.
 */
std::optional<BigInt> low_exponent_attack(const BigInt &cipherbytes, const BigInt &e) {
  return integer_root(cipherbytes, e);
}

struct RSA {
  BigInt n, e, d;

  void genkey(BigInt e_value, int bits = 512);

  Bytes pad(const Bytes &message) const;
  Bytes unpad(const Bytes &encoded) const;

  BigInt encrypt(const Bytes &message);
  Bytes decrypt(const BigInt &cipherbytes);
};

void RSA::genkey(BigInt e_value, int bits) {
  e = e_value;

  while (true) {
    BigInt p = random_prime(bits);
    BigInt q = random_prime(bits);
    if (p == q)
      continue;

    BigInt phi = (p - 1) * (q - 1);
    if (boost::multiprecision::gcd(e, phi) != 1)
      continue;

    n = p * q;
    d = mod_inverse(e, phi);
    return;
  }
}

/**
 * ----- PKCS#1 v1.5 padding --------
 * encoded = 0x00 || 0x02 || PS: Min 8-bit non-zero || 0x00 || M
 */
Bytes RSA::pad(const Bytes &message) const {
  size_t k = bytes_count(n);
  if (message.size() > k - 11)
    throw std::runtime_error("Message too long");

  Bytes encoded(k);
  encoded[0] = 0x00;
  encoded[1] = 0x02;

  static boost::random::mt19937 gen(std::random_device{}());
  boost::random::uniform_int_distribution<int> dist(1, 255); // no zero

  size_t ps_len = k - 3 - message.size();
  for (size_t i = 0; i < ps_len; i++)
    encoded[2 + i] = static_cast<uint8_t>(dist(gen));

  encoded[2 + ps_len] = 0x00;
  std::copy(message.begin(), message.end(), encoded.begin() + 3 + ps_len);

  return encoded;
}

Bytes RSA::unpad(const Bytes &encoded) const {
  if (encoded.size() < 11 || encoded[0] != 0x00 || encoded[1] != 0x02)
    throw std::runtime_error("Invalid padding");

  size_t i = 2;
  while (i < encoded.size() && encoded[i] != 0x00)
    i++;

  if (i < 10)
    throw std::runtime_error("Invalid padding");
  if (i == encoded.size())
    throw std::runtime_error("No separator");

  return Bytes(encoded.begin() + i + 1, encoded.end());
}

BigInt RSA::encrypt(const Bytes &message) {
  BigInt m = bytes_to_bigint(message);
  return pow_mod(m, e, n);
}

Bytes RSA::decrypt(const BigInt &cipherbytes) {
  size_t k = bytes_count(n);
  BigInt m = pow_mod(cipherbytes, d, n);
  return bigint_to_bytes_fixed(m, k);
}

void test_secure_rsa() {
  // Standard RSA (with padding and big e)
  std::cout << "=== SECURE RSA (padding + big e) ===\n";
  BigInt e = 65537;

  RSA rsa;
  rsa.genkey(e);

  std::string message = "Hello secure RSA!";
  Bytes msg_bytes(message.begin(), message.end());
  BigInt ciphertext = rsa.encrypt(rsa.pad(msg_bytes));
  std::cout << "Ciphertext: \n" << ciphertext << "\n";

  Bytes recovered_bytes = rsa.unpad(rsa.decrypt(ciphertext));
  std::string recovered(recovered_bytes.begin(), recovered_bytes.end());
  std::cout << "Secure RSA: " << recovered << "\n";
  std::cout << (recovered == message ? "PASS" : "FAIL") << '\n';
}

void test_low_exponent_attack() {
  // Insecure: without padding and small e
  std::cout << "=== INSECURE RSA (raw + small e) ===\n";
  BigInt e = 3;

  RSA rsa;
  rsa.genkey(e);

  std::string message = "Hi :(";
  Bytes message_bytes(message.begin(), message.end());

  BigInt ciphertext = rsa.encrypt(message_bytes);
  std::cout << "Ciphertext: \n" << ciphertext << "\n";

  auto recovered = low_exponent_attack(ciphertext, rsa.e);
  if (recovered) {
    auto recovered_data = recovered.value();
    auto recovered_message_bytes = bigint_to_bytes(recovered_data);
    std::string recovered_message(recovered_message_bytes.begin(), recovered_message_bytes.end());
    std::cout << "Recovered: " << recovered_message << '\n';
    std::cout << "SUCCESS\n";
  } else {
    std::cout << "Failed\n";
  }
}

int main() {
  test_secure_rsa();
  test_low_exponent_attack();

  return 0;
}
