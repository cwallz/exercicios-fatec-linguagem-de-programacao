//Exercício Extra 01
#include<iostream>
using namespace std;

int main (){
    
    double num1, num2, media;
    
    cout << "Por favor, digite a nota 1." << endl;
    cin >> num1;
    cout << "Por favor, digite a nota 2." << endl;
    cin >> num2;
    
    media = (num1 + num2) / 2;
    
    cout << "Sua média é " << media << "." << endl;
    
    if (media >= 10) {
        cout << "Excelente!" << endl;
    } else if (media >= 9) {
        cout << "Muito bom!" << endl;
    } else if (media >= 7) {
        cout << "Bom!" << endl;
    } else if (media >= 6) {
        cout << "Regular!" << endl;
    } else {
        cout << "Insuficiente!" << endl;
    }
    
    return 0;
}