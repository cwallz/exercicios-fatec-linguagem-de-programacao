//Exercício 13
#include<iostream>
using namespace std;

int main() {

    int num, resultado;
    
    do {
        cout << "Informe um número inteiro positivo." << endl;
        cin >> num;
        
        if (num < 0) {
            cout << "Número inválido." << endl;
        }
    } while (num < 0);
    
    cout << "TABUADA DO NÚMERO... " << num << "." << endl;
    
    for (int i = 1; i <= 10; i++) {
        resultado = i * num;
        cout << num << " X " << i << " = " << resultado << "." << endl;
    }
    
    
    cout << "Tarefa concluída." << endl;
    
    return 0;
}