//Exercício 18
#include<iostream>
using namespace std;

void quadrado(int a);

int main() {
    
    int num;
    
    cout << "Por favor, digite um número inteiro para que possamos calcular seu quadrado." << endl;
    cin >> num;
    
    quadrado (num);
    
    cout << "Tarefa concluída." << endl;
    
    return 0;
}

void quadrado(int a){
    
    int resultado;
    
    resultado = a * a;
    cout << "O quadrado de " << a << " é " << resultado << endl;
    
}