//Exercício 9
#include<iostream>
using namespace std;

int main() {

    int num1, num2, num3;
    
    cout << "Informe o primeiro número." << endl;
    cin >> num1;
    cout << "Informe o segundo número." << endl;
    cin >> num2;
    cout << "Informe o terceiro número." << endl;
    cin >> num3;
    
    if (num1 > num2 && num1 > num3) {
        cout << "O maior número mencionado é o " << num1 << "." << endl;
    } else if (num2 > num1 && num2 > num3) {
        cout << "O maior número mencionado é o " << num2 << "." << endl;
    } else {
        cout << "O maior número mencionado é o " << num3 << "." << endl;
    }
    

    return 0;
}
