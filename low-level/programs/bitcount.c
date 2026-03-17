#include <ctype.h>
#include <stdio.h>
#include <string.h>

int bitcount(unsigned x) {
    int b;

    // each iteration deletes the rightmost 1-bit
    for (b = 0; x != 0; x &= x - 1, ++b);

    return b;
}

int main() {
    int num = 15;

    printf("%d = %d\n", num, bitcount(num));

    return 0;
}