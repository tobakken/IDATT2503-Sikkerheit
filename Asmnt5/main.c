#include "utility.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  char msg[] = "Is 3 < 4 && 3 > 4?";
  printf("%s becomes: %s \n", msg, encode(msg));
}
