// Exercício 1 - Aula 25 set 2025
// Nome: Carlos Wallace Pereira

#include <iostream>
#include <stdlib.h>
#define N 10
using namespace std;


void vetorDosQuadrados(double quadrados[], int tamanhoVetor) {
    cout << endl << "Vetor dos quadrados: ";
    for (int i = 0; i < tamanhoVetor; i++) {
        cout << quadrados[i] << " ";
    }
    cout << endl;
}

//----------------------
//Onde o código começa:
//----------------------

int main() {
    double numeros[N];    
    double quadrados[N];  

    cout << "============================================" << endl;
    cout << "Por favor, digite " << N << " numeros reais:" << endl;
    cout << "============================================" << endl << endl;
    for (int i = 0; i < N; i++) {
        cout << "Numero " << i+1 << ": ";
        cin >> numeros[i];
        quadrados[i] = numeros[i] * numeros[i];
        system("clear");
    }

    cout << "============================================" << endl;
    cout << "Vetor digitado: ";
    for (int i = 0; i < N; i++) {
        cout << numeros[i] << " ";
    }

    vetorDosQuadrados(quadrados, N);
   
    cout << "============================================" << endl << endl;
    cout << "Tarefa concluída." << endl;
   
    return 0;
}