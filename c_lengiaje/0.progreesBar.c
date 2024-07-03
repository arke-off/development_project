// Created by Infinity

#include <stdio.h>

int main()
{
    int i,j;
    printf("Loading...\n");
    for(i=0;i<=20;i++)
    {
        for(j=0;j<i;j+=1)
        printf("*");
        printf("%d%%",i*5);
        printf("\n");
    }
    printf("\n");
    printf("Fully Loaded!");
    printf("\n\n\n\n\n");
    return 0;
}