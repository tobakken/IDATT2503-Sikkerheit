#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *replace(const char *msg, const char *old, const char *new) {
  char *result;
  int i, count = 0;
  int newLength = strlen(new);
  int oldLength = 1;

  // counting number of occurences of old
  for (i = 0; msg[i] != '\0'; i++) {
    if (strstr(&msg[i], old) == &msg[i]) {
      count++;
    }
  }
  result = (char *)malloc(i + count * (newLength - oldLength) + 1);

  i = 0;
  while (*msg) {
    if (strstr(msg, old) == msg) {
      strcpy(&result[i], new);
      i += newLength;
      msg++;
    } else
      result[i++] = *msg++;
  }

  result[i] = '\0';
  return result;
}

char *encode(const char *msg) {
  return replace(replace(replace(msg, "&", "&amp;"), "<", "&lt;"), ">", "&gt;");
}

int main() {
  char msg[] = "Is 3 < 4 && 3 > 4?";
  printf("%s becomes: %s", msg, encode(msg));
}
