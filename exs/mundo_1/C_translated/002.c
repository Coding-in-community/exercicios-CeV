/*
    002 - Replying to user
   Create a  script that reads a person's name and displays a message
    welcome according to the value entered

    
*/

#include <stdio.h>

int main(void)
{
    char name[50];
    printf("What is your name? ");
    scanf("%s", &name);
    printf("Welcome, %s!\n", name);
    return 0;
}