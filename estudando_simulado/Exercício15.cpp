//Exercício 15
#include<iostream>
using namespace std;

int main() {

    int num, cont = 0;
    
    
    for (int i = 1; i <= 10; i++) {
        do {
            cout << "Digite o " << i << "° número inteiro positivo de uma sequência de 10." << endl;
            cin >> num;
            
            if (num < 0) {
                cout << "Número inválido." << endl;
            }
        } while (num < 0);
        
        if (num % 2 == 0) {
            cont = cont + 1;
        }
    }
    
    cout << "Dos números digitados, temos " << cont << " par(es)." << endl;
    cout << "Tarefa concluída." << endl;
    return 0;
}
