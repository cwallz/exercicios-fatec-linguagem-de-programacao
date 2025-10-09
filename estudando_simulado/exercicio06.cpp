//Exercício 6
#include<iostream>
using namespace std;

int main() {
    int num;
    
    cout << "Digite um número." << endl;
    cin >> num;
    
    if (num == 0) {
        cout << "Esse número é zero." << endl;
    } else if (num < 0) {
        cout << "Esse número é negativo." << endl;
    } else {
        cout << "Esse número é positivo." << endl;
    }
    
    return 0;
}
