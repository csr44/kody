#include <stdio.h>
#include <stdlib.h> //zoradte napoje alko nealko podla nazvu, promile, vyrobca a posledny parameter objem balenia
#include <string.h> // rozsirit o cenu, piata hodnota cena, cena sa bude vzdy lisit float cena//pred porovnej cisla 

typedef struct
{
    char * nazev;
    float promile;
    char * vyrobce;
    float objemBaleni;
    float cena;
}
tNapoj;

int porovnejCisla(float a, float b)
{
    if (a<b) return -1;
    if (a>b) return 1;
    return 0;
}
int porovnejNapoje(const void *n1, const void *n2) //
{
    if ((strcmp(((tNapoj*)n1)->nazev, ((tNapoj*)n2)->nazev))==0) //strikomper
        //porovnanie, ci maju rovnaky nazov, ak ano, funkciu strcmp sa vrati 0
        {
            if(porovnejCisla(((tNapoj*)n1)->promile, ((tNapoj*)n2)->promile)==0) //fncia porovnej cisla
                //dale porovnava podle promile, vyrobce, objemBaleni
                {
                    if((strcmp(((tNapoj*)n1)->vyrobce,((tNapoj*)n2)->vyrobce))==0)
                    {
                         if((porovnejCisla(((tNapoj*)n1)->objemBaleni,((tNapoj*)n2)->objemBaleni))==0)
                            {
                                porovnejCisla(((tNapoj*)n1)->cena, ((tNapoj*)n2)->cena);
                            }
                        else return porovnejCisla(((tNapoj*)n1)->objemBaleni, ((tNapoj*)n2)->objemBaleni);
                    }
                    else return strcmp(((tNapoj*)n1)->vyrobce, ((tNapoj*)n2)->vyrobce);
                }
                else return porovnejCisla(((tNapoj*)n1)->promile, ((tNapoj*)n2)->promile);
        }
        else return strcmp(((tNapoj*)n1)->nazev, ((tNapoj*)n2)->nazev);
}
    tNapoj poleNapoju[]={
    {"Pivo", 3.5,"Gambrinus", 0.5, 40}, //tieto riadky ako jeden prvok
    {"Pivo",3,"Gambrinus",1,32},
    {"Pivo",3.5,"Krusovice",0.5,33},
    {"Pivo",3,"Gambrinus",0.5,35},
    {"Vino",6.5,"Templarske",0.7,150},
    {"Lih",45,"Amundsen",1.0,300},
    {"Pivo",4,"Plzen",0.5,38},
    {"Vino",7.5,"Valtice",1.0,180},
    {"Vino",7,"Vino Mikulov",1.0,170},
    {"Arum",45,"Bozkov",1.0,140},
    {"Absinth",70,"Jelinek",0.7,420},
    {"Pivo",4,"Staropramen",0.5,30},
    {"Vodka",25,"Bozkov",0.5,125},
    
    };
    //vsetko nad tymto prebehne vramci deklarace
    int main()
    {
        printf ("\n-------------------------------------------------------\n");
        printf (" Nazev       Promile\tVyrobce        Objem        Cena    ");
        printf("\n=========================================================");
        
    int z;
    int pocetPrvku=sizeof(poleNapoju)/sizeof(tNapoj);
    
    qsort(poleNapoju,pocetPrvku, sizeof(tNapoj),&porovnejNapoje); //fcia qsort - algoritmus, zoradenie pola-- potrebuje vsetky styry
    //&porovnejNapoje prepe do funkce porovnej napoje..........tisk jednotlivych polozek pole
    for(z=0;z<pocetPrvku; z++)
        
        printf("\n %s \t%2.1f \t%s  \t%0.1f l \t%0.1f l", poleNapoju[z].nazev, //pribudne pole napojov, cena
        (poleNapoju+z)->promile, (poleNapoju+z)->vyrobce, (poleNapoju+z)->objemBaleni, (poleNapoju+z)->cena);
        
        printf ("\n\n");
        return 0;
    }
    