#include <stdio.h>

int main() {
    // 1 byte
    unsigned char us_char = 0;
    // 2 bytes
    unsigned short us_short = 0;
    // 4 bytes
    unsigned int us_int = 0;
    // 8 bytes
    unsigned long us_long = 0;

    
    printf("unsigned char: %d <= x <= %d\n", us_char, (unsigned char) (us_char - 1));
    printf("unsigned short: %d <= x <= %d\n", us_short, (unsigned short) (us_short - 1));
    printf("unsigned int: %d <= x <= %d\n", us_int, us_int - 1);
    // %u -> printf reads lowest 32 bits of the value passed
    // %lu -> printf reads lowest 64bits of the value passed
    printf("unsigned long: %d <= x <= %lu\n", us_long, (unsigned long) (us_long - 1));

    return 0;
}