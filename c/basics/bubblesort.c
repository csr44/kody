#include <stdio.h>
int main(void)
{
	int pole[]={7, 6, 4, 2, 8, 0, 3, 5, 1, 9, 10, 12};
	int pocet=sizeof(pole)/sizeof(int); // po 4bity
	int a, b, pomocna,priechody;
    priechody=0;
   printf("Nezoradene hodnoty: \n");
        for(a=0; a<pocet; a++)
        {
        printf("%d", pole [a]); 
        }
for(b=1; b<pocet; b++) //deklarovana premenna B je to len kvôli priechodom, kvôli nim bol spravena for
        {   priechody++;
            for(a=1; a<pocet; a++)
            {
               if(pole[a-1]>pole[a]) // a mínus 1 .... index 0 a index 1
                {
                   pomocna=pole[a];
                   pole[a]=pole[a-1]; // preco??
                   pole[a-1]=pomocna;
                }
            }
                
        }
printf("\nZoradene hodnoty: \n");
for(a=0; a<pocet;a++)
{
    printf("%d", pole[a]);
}
printf("\nPocet priechodov: %d ", priechody);
}
