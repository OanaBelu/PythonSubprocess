#include <stdio.h>
#include <conio.h>
#include <math.h>

void main(void)
{
    int optiune;
    float x;


    printf("\nSelect one option from the menu : ");
    printf("\n1 - Functia exponent");
    printf("\n2 - Functia logaritm natural");
    printf("\n3 - Functia modul");
    printf("\n4 - Functia putere ");
    printf("\nEnter your option: ");
    scanf("%d", &optiune);

    switch(optiune){
        case 1: printf("Enter a natural number x, x="); scanf("%f",&x);
            printf("\nExponent de x :  e^%.2f = %.2f",x, exp(x)); break;
        case 2: printf("Enter a natural positive number x, x="); scanf("%f",&x);
            if (x<0)
                printf("\nYour number must be positive.");
            else
                printf("\nLogaritm natural : ln(%.2f) = %.3f",x, log(x));break;
        case 3: printf("Enter a natural number x, x="); scanf("%f",&x);
            printf("\nModul : |%.2f| = %.2f",x, fabs(x));break;
        case 4: printf("Enter a natural number x, x="); scanf("%f",&x);
            printf("\n\n 10 la puterea x, 10^%.2f = %.3f",x,pow(10,x));break;
        default: printf("\nYour option does not exist in the menu.");
    }

}