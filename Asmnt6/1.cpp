#include <iomanip>
#include <iostream>
#include <openssl/evp.h>
#include <openssl/sha.h>
#include <sstream>
#include <string>

using namespace std;

/// Return hex string from bytes in input string.
std::string hex(const std::string &input) {
  std::stringstream hex_stream;
  hex_stream << std::hex << std::internal << std::setfill('0');
  for (auto &byte : input)
    hex_stream << std::setw(2) << (int)(unsigned char)byte;
  return hex_stream.str();
}

/// Return the SHA-512 (512-bit) hash from input.
std::string sha512(const std::string &input) noexcept {
  auto evp_md = EVP_sha512();

  std::string hash(SHA512_DIGEST_LENGTH, '\0');

  auto ctx = EVP_MD_CTX_create();
  EVP_MD_CTX_init(ctx);
  EVP_DigestInit_ex(ctx, evp_md, nullptr);
  EVP_DigestUpdate(ctx, input.data(), input.size());
  EVP_DigestFinal_ex(ctx, reinterpret_cast<unsigned char *>(&hash[0]), nullptr);
  EVP_MD_CTX_destroy(ctx);

  return hash;
}

std::string pbkdf2(const std::string &password, const std::string &salt) {
  std::string hash;
  hash.resize(20);
  PKCS5_PBKDF2_HMAC_SHA1((const char *)&password[0], password.size(), (const unsigned char *)&salt[0], salt.size(), 2048, 20, (unsigned char *)&hash[0]);
  return hash;
}

void brute_force_recurisvely(string pwd, int pos, int size) {
  if (pos < size) {
    for (int i = 48; i < 122; ++i) {
      pwd[pos] = char(i);
      string res = hex(pbkdf2(pwd, "Saltet til Ola"));
      if (res == "ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6") {
        cout << "Password is: " << pwd << endl;
      }
      // cout << pwd << endl;
      //  cout << res << endl;
      brute_force_recurisvely(pwd, pos + 1, size);
    }
  }
}

void brute_force(size_t max) {
  string pwd = "";

  for (size_t i = 0; i < max; ++i) {
    brute_force_recurisvely(pwd, 0, i);
    pwd.append("a");
  }
}

int main() {
  brute_force(4);
}
