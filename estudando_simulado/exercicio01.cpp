//Exercício1
#include<iostream>
using namespace std;

int main() {
    int num1, num2;
    int soma;
    
    cout << "Por favor, digite o primeiro número." << endl;
    cin >> num1;
    cout << "Por favor, digite o segundo número." << endl;
    cin >> num2;
    
    soma = num1 + num2;
    
    cout << "A soma dos números " << num1 << " e " << num2 << " é... " << soma << "!" << endl;
    
    return 0;
}