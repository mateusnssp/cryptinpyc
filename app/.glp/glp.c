#include<stdio.h>
#include<stdlib.h>



int main(){


    int a=10000,b,c,n=50000,d;           //Declarando as variáveis







    d=n*(-1);

      printf("Os primeiros %i numeros primos sao:\n",n);

            //ABRIR ARQUIVO
            FILE *arq;
            arq = fopen("lp.txt", "w");

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
      


            //FECHAR ARQUIVO
            fclose(arq); 

      
      printf("\n\n"); 





    return 0;
}           