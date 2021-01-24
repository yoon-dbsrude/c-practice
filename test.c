#include <stdio.h>

int main()
{
    int name[10];
    printf("What's your name?\n");
    scanf("%s", name);
    printf("hello, %s!\n", name);
    return 0;
}