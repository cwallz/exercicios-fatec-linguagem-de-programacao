//Exercício 8
#include<iostream>
using namespace std;

int main() {

    double num1, num2, media;
    
    cout << "Informe o primeiro número." << endl;
    cin >> num1;
    cout << "Informe o segundo número." << endl;
    cin >> num2;
    
    media = ( num1 + num2 ) / 2;
    
    cout << "A sua média é... " << media << "." << endl;
    
    if (media >= 6) {
        cout << "Portanto, você está aprovado!" << endl;
    } else {
        cout << "Portanto, você está reprovado!" << endl;
    }

    return 0;
}