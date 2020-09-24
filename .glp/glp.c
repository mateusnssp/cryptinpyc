#include<stdio.h>
#include<stdlib.h>



int main(){


    int a=0,b,c,n=100,d;           //Declarando as variáveis



    //ABRIR ARQUIVO
    FILE *arq;
    arq = fopen("lp.txt", "w");




    d=n*(-1);

      printf("Os primeiros %i numeros primos sao:\n",n);


    do        
    {  a++;    
        c=0;

        for(b=1;b<a;b++)
            if(a%b==0)
            c++;


        //SE FOR PRIMO
        if(c==1){





            printf("%i\n",a);    
    



            fprintf(arq, "%d\n", a);




            d++;
        }
    }while(d); 
      



      
      printf("\n\n"); 




    //FECHAR ARQUIVO
    fclose(arq); 

    return 0;
}           