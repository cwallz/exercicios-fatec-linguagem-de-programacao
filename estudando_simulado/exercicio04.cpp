//Exercício 4
#include<iostream>
using namespace std;

int main() {
    double num1, num2, media;
    
    cout << "Por favor, digite o primeiro número." << endl;
    cin >> num1;
    cout << "Por favor, digite o segundo número." << endl;
    cin >> num2;
    
    media = (num1 + num2) / 2;
    
    cout << "A média dos números digitados é... " << media << "." << endl;
    
    
    
    return 0;
}