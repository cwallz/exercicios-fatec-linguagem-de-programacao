//Exercício 20
#include<iostream>
using namespace std;

void parOuImpar(int a);

int main() {
    
    int num;
    
    cout << "Por favor, digite um número inteiro positivo." << endl;
    cin >> num;
    
    parOuImpar(num);
    
    cout << "Tarefa concluída." << endl;
    
    return 0;
}


void parOuImpar (int a){
    
    if (a % 2 == 0) {
        cout << "O número informado é par." << endl;
    } else {
        cout << "O número informado é ímpar." << endl;
    }
    
}
