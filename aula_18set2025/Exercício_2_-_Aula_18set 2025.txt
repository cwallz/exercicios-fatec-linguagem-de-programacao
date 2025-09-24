// Exercício 2 - Aula 18 set 2025
// Nome: Carlos Wallace Pereira

#include <iostream>
using namespace std;

void identificarPar (int numero) {
    
    if (numero % 2 != 0){
        cout << "Esse número é impar." << endl;
    } 
    else {
        cout << "Esse número é par." << endl;
    }
    
};

void identificarPrimo (int numero) {
    
    bool primo = true;
    
    if (numero <= 1) {
        cout << "Esse número não é primo." << endl;
    }
    
    for (int i = 2; i <= numero / 2; i++) {
        if (numero % i == 0) {
            primo = false;
            break;
        }
    }

    if (primo) {
        cout << "Esse número é primo." << endl;
    } else {
        cout << "Esse número não é primo." << endl;
    }
    
};


int main() {
    
    int numero;

    cout << "Digite um número inteiro:" << endl;
    cin >> numero;
    
    identificarPar (numero);
    
    identificarPrimo (numero);
    
    return 0;
}
