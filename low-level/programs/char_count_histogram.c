#include <stdio.h>

// Print a histogram including the counts of letter characters, digit characters and other characters.
void print_histogram(int letter_count, int digit_count, int other_count, int total_char_count) {
    printf(" 0");

    for (int i = 1; i <= total_char_count; ++i)
        printf(" %3d", i);

    printf("\n");

    char letter_bar[4 * letter_count + 1];

    for (size_t i = 0; i < 4 * letter_count; ++i)
        letter_bar[i] = '+';

    letter_bar[4 * letter_count] = '\0';

    char digit_bar[4 * digit_count + 1];

    for (size_t i = 0; i < 4 * digit_count; ++i)
        digit_bar[i] = '+';

    letter_bar[4 * letter_count] = '\0';

    char other_bar[4 * other_count + 1];

    for (size_t i = 0; i < 4 * other_count; ++i)
        other_bar[i] = '+';

    other_bar[4 * other_count] = '\0';

    printf("l|%s\nd|%s\no|%s\n", letter_bar, digit_bar, other_bar);
}

int main() {
    int letter_count, digit_count, other_count, total_char_count, c;

    letter_count = digit_count = other_count = total_char_count = 0;

    while ((c = getchar()) != EOF) {
        ++total_char_count; 

        if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) {
            ++letter_count;
        }
        else if (c >= '0' && c <= '9') {
            ++digit_count;
        }
        else {
            ++other_count;  
        }
    }

    print_histogram(letter_count, digit_count, other_count, total_char_count);

    return 0;
}
