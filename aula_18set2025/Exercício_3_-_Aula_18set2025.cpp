// Exercício 3 - Aula 18 set 2025
// Nome: Carlos Wallace Pereira
#include <iostream>
using namespace std;


float calcularPesoIdeal (float altura, char genero) {
    
    float pesoIdeal;


    altura = altura / 100.0;
   
    if (genero == 'h' || genero == 'H') {
        pesoIdeal = (72.7 * altura - 58);
    } else {
        pesoIdeal = (62.1 * altura - 44.7);
    }
        
    return pesoIdeal;
    
};

int main() {
    
    float altura;
    char genero;

    cout << "========================================================" << endl;
    cout << "Esse programa irá calcular seu peso ideal de acordo com " << endl;
    cout << "seu gênero e altura." << endl;
    cout << "========================================================" << endl;
    
    
    do {
        cout << "Nos informe seu gênero. Sendo: " << endl;
        cout << " H - homem" << endl;
        cout << " M - mulher" << endl;
        cin >> genero;
    
    } while (genero != 'h' && genero != 'H' && genero != 'm' && genero != 'M');
    
    
    do {
        cout << "Por favor, digite a sua altura em cm." << endl;
        cin >> altura;
    
    } while (altura<0 || altura>=300);
    
    
    float pesoIdeal = calcularPesoIdeal (altura, genero);
    
    cout << endl << "Seu peso ideal é " << pesoIdeal << "!" << endl;
    
    
    return 0;
    
    
}