#include <stdio.h>

int main() {
    printf("char : %zu byte(s)\n", sizeof(char));
    printf("short : %zu byte(s)\n", sizeof(short));
    printf("int : %zu byte(s)\n", sizeof(int));
    printf("long : %zu byte(s)\n", sizeof(long));
    printf("long long : %zu byte(s)\n", sizeof(long long));

    printf("float : %zu byte(s)\n", sizeof(float));
    printf("double : %zu byte(s)\n", sizeof(double));
    printf("long double : %zu byte(s)\n", sizeof(long double));

    return 0;
}