#include <iostream>

using namespace std;

string replace(string msg, string replace_char, string replace_with) {
  size_t index = 0;
  while (index < msg.length()) {
    index = msg.find(replace_char, index);
    if (index == string::npos)
      break;
    else {
      msg = msg.substr(0, index) + replace_with + msg.substr(index + 1);
    }
    index += replace_with.length();
  }
  return msg;
}

// Horrible memory usage, can't be bothered to fix it, such a stupid task
string encode(string msg) {
  msg = replace(msg, "&", "&amp;");
  msg = replace(msg, "<", "&lt;");
  msg = replace(msg, ">", "&gt;");
  return msg;
}

int main() {
  string msg = "3 & 4";
  string msg2 = "3 < 4";
  string msg3 = "3 > 4";
  string msg4 = "Is 3 < 4 && 3 > 4?";

  cout << msg << " becomes: " << encode(msg) << endl;
  cout << msg2 << " becomes: " << encode(msg2) << endl;
  cout << msg3 << " becomes: " << encode(msg3) << endl;
  cout << msg4 << " becomes: " << encode(msg4) << endl;
}
