// Exercício 1 - Aula 18 set 2025
// Nome: Carlos Wallace Pereira

#include <iostream>
using namespace std;

void calc_fatorial(int numero) {
    long fatorial = 1;
    for (int i = 1; i <= numero; i++) {
        fatorial *= i;
    }
    cout << numero << "! = " << fatorial << endl; 
}

int main() {
    int numero;
   
    while(true){
        cout << "Digite um valor inteiro e positivo para calcular seu fatorial." << endl;
        cout << "Ou digite -1 para sair." << endl;
        cin >> numero;
       
        if (numero == -1){
            cout << "Você saiu do programa." << endl;
            break;
        }
       
        if (numero < 0){
            cout << "Número inválido. Tente novamente." << endl;
            continue;
        }

        calc_fatorial(numero);
    }
   
    return 0;
}
