#include <stdio.h>

int main() {
    int age;
    float height;
    char grade;
    char name[20];

    // Asking user for input 
    printf("Enter your age, height, grade, and name: ");

    // Reading input from user 
    // (Notice: variables are OUTSIDE the quotes, separated by commas. No '&' for name)
    scanf("%d %f %c %s", &age, &height, &grade, name);

    // Displaying the results 
  
    printf("Your age: %d \n", age);
    printf("Your height: %.2f \n", height);
    printf("Your grade: %c \n", grade);
    printf("Your name: %s \n", name);

    return 0;
}