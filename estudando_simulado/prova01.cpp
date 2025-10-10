//Exercício da prova 1 
#include <iostream>
using namespace std;

int main (){
    int num;
    
    do {
        cout << "Digite um número inteiro positivo." << endl;
        cin >> num;
            if (num < 0 || num % 2 != 0) {
                cout << "Número inválido." << endl;
            }
    } while (num < 0 || num % 2 != 0);
    
    while (num >= 0) {
        cout << num << endl;
        num = num - 2;
    }
    cout << "Tarefa concluída." << endl;
    
    return 0;
}
