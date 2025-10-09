//Exercício 7
#include<iostream>
using namespace std;

int main() {
    int num;
    
    cout << "Digite um número." << endl;
    cin >> num;
    
    if (num % 2 == 0) {
        cout << "Esse número é par." << endl;
    } else {
        cout << "Esse número é ímpar." << endl;
    }
    
    return 0;
}
