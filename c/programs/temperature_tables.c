#include <stdio.h>

// Print a fahrenheit to celsius table
void print_fahr_to_cels_table() {
    float fahr, celsius;
    float lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;
    
    fahr = lower;

    printf("Fahrenheit\tCelsius\n");

    while (fahr <= upper) {
        celsius = (5.0  / 9.0) * (fahr - 32.0);

        printf("%10.0f\t%7.1f\n", fahr, celsius);

        fahr = fahr + step;
    }
}

// Print a celsius to fahrenheit table
void print_cels_to_fahr_table() {
    float fahr, celsius;
    float lower, upper, step;

    lower = 0;
    upper = 150;
    step = 10;

    celsius = lower;

    printf("Celsius\tFahrenheit\n");

    while (celsius <= upper) {
        fahr = (9.0 / 5.0) * celsius + 32.0;

        printf("%7.0f\t%10.1f\n", celsius, fahr);

        celsius = celsius + step;
    }

}

int main() {
    print_cels_to_fahr_table();
    print_fahr_to_cels_table();
}

