#include <stdio.h>
#include <math.h> // matematicka funkcia
int main(void)
{
    double x1,x2,x,xlin,r,i,a,b,c; //dvojta presnost 8 bitov
    printf("\nVypocet korenu kvadraticke rovnice - ax^2+bx+c=0");
    printf("\nZadajte hodnotu a,b,c (iba cele cisla):");

    while(scanf("%lf %lf %lf",&a,&b,&c)!=3) //while cykl pre overenie
    {
        printf("zadavajte iba cisla!!!\n");
        fflush(stdin);
    }
    
    printf("\n%.01fx^2+%.01fx+%.01f=0",a,b,c);  //vypisanie kvadratickej rovnice v prislusnom tvare (cele cisla a x2)
    if(a==0)
        {
    xlin=-(c/b); //dopocitane linearne x
    printf("x = %1f \n", xlin);
    return 0;  //pre ukoncenie
        }
double D; //deklaracia diskriminantu //na realne cele cislo//%lf - long float
D=(pow(b,2)-(4*a*c));  //prva matematicka funkcia - ma dva vstupne parametry
int A = (1*(D==0))+ (2*(D>0))+(4*(D<0)); //priradenie bude posldne co sa stane, vysledok sa zapise do A
switch(A)// 3stavy}

        {
   
    case 1:
    printf("\nRovnice ma jeden koren: \n");
    x=(-b+sqrt(D))/(2*a);
    printf("x=%lf\n",x);
    break; //break opusti telo switcha, a chod na return 0
    
    case 2:
    printf("\nRovnice ma dva realne koreny: \n");
    x1=(-b+sqrt(D))/(2*a); 
    x2=(-b-sqrt(D))/(2*a);
    printf("x1=%lf\n", x1);
    printf("x2=%lf\n", x2);
    break;
    case 4:
     printf("\nRovnice ma komplexne riesenie: \n");
    r=(-b)/(2*a); 
    i=(sqrt(-1*D))/(2*a);
    printf("r=%.2lf\n", r);
    printf("i=%.2lf\n", i);
    break;
        }
        return 0;
}
