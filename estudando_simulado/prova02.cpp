//Exercício da prova 2 
#include <iostream>
using namespace std;

void fatorial (int a);

int main (){
    int num;
    
    do {
        cout << "Digite um número inteiro positivo." << endl;
        cin >> num;
            if (num < 0) {
                cout << "Número inválido." << endl;
            }
    } while (num < 0);
    
    fatorial(num);
    cout << "Tarefa concluída." << endl;
    
    return 0;
}

void fatorial (int a){
    long resultado = 1;
    
    for (int i = 1; i <= a; i++){
        resultado = resultado * i;
    }
    cout << "O fatorial de "<< a << "! é " << resultado << "." << endl;
}