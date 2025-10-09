//Exercício 14
#include<iostream>
using namespace std;

int main() {

    int n, resultado = 0;
    
    do {
        cout << "Por favor, digite um número inteiro positivo." << endl;
        cin >> n;
        
        if (n < 0) {
            cout << "Número inválido." << endl;
        }
    } while (n < 0);
    
    
    if (n == 0) {
        cout << "A somatória do número digitado é 0.";
    } else {
        for (int i = 1; i <= n; i++) {
            cout << i;
                if (i != n) {
                    cout << " + ";
                }
            resultado = resultado + i;
        }
        cout << endl << "A somatória do número digitado é " << resultado << "." << endl;
    }
    
    cout << "Tarefa concluída." << endl;
    return 0;
}