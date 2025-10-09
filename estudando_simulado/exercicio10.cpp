//Exercício 10
#include<iostream>
using namespace std;

int main() {

    int idade;
    
    cout << "Por favor, nos informe a sua idade." << endl;
    cin >> idade;
    
    if (idade < 12) {
        cout << "Você é uma criança." << endl;
    } else if (idade >= 12 && idade <= 17) {
        cout << "Você é um adolescente." << endl;
    } else {
        cout << "Você é um adulto." << endl;
    }

    return 0;
}
