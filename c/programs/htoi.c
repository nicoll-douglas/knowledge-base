#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>

int htoi(const char hex[]) {
    int i = 0;
    int n = 0;

    if (hex[i] == '0') {
        ++i;

        if (hex[i] == 'x' || hex[i] == 'X') ++i;
    }

    for (; hex[i] != '\0'; ++i) {
        int digit;

        if (hex[i] >= '0' && hex[i] <= '9')
            digit = hex[i] - '0';
        else {
            char letter = tolower(hex[i]);

            if (letter >= 'a' && letter <= 'f')
                digit = letter - 'a' + 10;
            else 
                break;
        }

        // check if new value of n (n * 16 + digit) overflows
        if (n > (INT_MAX - digit) / 16)
            return -1;

        n = 16 * n + digit;
    }

    return n;
}

int main() {
    char hex[] = "0xAB35";

    printf("%s = %d\n", hex, htoi(hex));

    return 0;
}