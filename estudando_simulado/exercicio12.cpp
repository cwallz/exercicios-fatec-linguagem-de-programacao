//Exercício 12
#include<iostream>
using namespace std;

int main() {

    int num;
    
    do {
        cout << "Escreva um número inteiro positivo." << endl;
        cin >> num;
        
        if (num < 0) {
            cout << "Número inválido." << endl;
        }
    } while (num < 0);  
    
    cout << "A ordem do número 0 ao seu número escolhido é:" << endl;
    
    for (int i = 0; i <= num; i++) {
        cout << i << endl;
    }
    
    cout << "Tarefa realizada.";
    
    return 0;
}
