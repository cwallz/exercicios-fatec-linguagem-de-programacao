//Exercício da prova 4
#include <iostream>
using namespace std;

int main (){
    
    int cont = 1, aux = 0;
    
    while (cont <= 5){
        if (cont % 2 != 0) {
            aux = aux + cont;
        }
        cont++;
    }
    
    cout << aux << endl;
    
    return 0;
}