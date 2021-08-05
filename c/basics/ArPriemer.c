#include <stdio.h>
FILE *vstup,*vystup;
int main(int argc, char**argv) //

{
    char subor[256]; //deklaracia retazcov
    char meno[25];
    char priezvisko[25]; //index, definovanie pola o 25 znakoch
    float sucet=0; 
    float znamka=0;
    float priemer=0;
    int pocetziakov; 
    pocetziakov=0; //promenna, pocet
    
    
    if(argc>1)
    {   
        vstup=fopen(argv[1], "r");
        if(vstup==NULL)
            {
            printf("\nVstupny suber nie je mozne otvorit\n");
            return 1;
            }
    }
    else{
        printf("\nZadajte nazov vystupneho suboru: "); //ak to neprecital..
        gets(subor);
        vstup=fopen(subor,"r");
        if(vstup==NULL){
            printf("\nVstupny subor nie je mozne otvorit");
            return 1;
                        }   
        
        }
    if(argc>2){
        vystup=fopen(argv[2], "w");
        if (vystup==NULL)
            {
            printf("\nVystupny subor nie je mozne otvorit\n");
            return 1;
            }
                }
    else{
        printf("\nZadajte nazov vstupneho suboru: ");
        gets(subor);
        vystup=fopen(subor,"w");
        if(vystup==NULL)
        {
            printf("\nVstupny subor nie je mozne otvorit");
            return 1;
        }
        }
    while(fscanf(vstup,"%s%s%f",&meno,&priezvisko,&znamka)!=EOF) //%s text, text potom %fcislo/nacitam meno priezvisko znamka a to cele robim tak dlho az kym nenarazaim na EO file
    {
        priemer += znamka; 
        pocetziakov++;
        printf("\n%s %s %0.2f",meno,priezvisko,znamka); //jedna premenna musi byt stale inkrementoana - pocet
        fprintf(vystup,"\n%s %s %0.2f", meno,priezvisko,znamka); //druha premenna sucet bude stale navysovana o hodnotu
    }
    printf("\nCelkovy priemerny prospech: %0.2f", priemer/pocetziakov);
    fprintf(vystup, "\nCelkovy priemerny prospech: %0.2f\n", priemer);
    fclose(vstup);
    fclose(vystup);
    return 0;
}
