//Exercício Extra 02
#include<iostream>
using namespace std;

void soma(int a, int b);
void subtracao(int a, int b);
void restoDivisao(int a, int b);
void fatorial(int a);


int main (){
    
    int num1, num2;
    
    cout << "Digite o primeiro número." << endl;
    cin >> num1;
    cout << "Digite o segundo número." << endl;
    cin >> num2;
    
    soma(num1, num2);
    subtracao(num1, num2);
    restoDivisao(num1, num2);
    fatorial(num1);
    fatorial(num2);
    
    cout << "Tarefa concluída.";
    
    return 0;
}

void soma(int a, int b){

    int resultado;
    
    resultado = a + b;
    cout << "A soma de " << a << " + " << b << " = " << resultado << endl;
    
}    
    
void subtracao(int a, int b){

    int resultado;
    
    resultado = a - b;
    cout << "A subtração de " << a << " - " << b << " = " << resultado << endl;
    
}  

void restoDivisao(int a, int b){

    int resultado; 
    
    if (b == 0) {
        cout << "Não existe divisão por zero." << endl;
    } else { 
        resultado = a % b;
        cout << "O resto da divisão de " << a << " / " << b << " = " << resultado << endl;
    }
}   

void fatorial(int a){

    long resultado = 1;
    
    if (a < 0){
        cout << "Não existe fatorial de número negativo." << endl;
    } else{
        for (int i = 1; i <= a; i++){
            resultado = resultado * i;
        }
        cout << "O fatorial do número " << a << "! é " << resultado << endl;
    }
}    