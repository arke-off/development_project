//libreria y declaracionces
#include <stdio.h>
int i=0;
int vector[10];


//llenar un vector con valores random del 0 al 10
while(i<=10){
    vector[i]=rand()%10+1;
    i++;
}
//imprimir el vector
i=0;
while(i<10){
    printf("%d \t",vector[i]);
    i++;
    Sleep(100);
}