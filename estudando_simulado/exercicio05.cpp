//Exercício 5
#include<iostream>
using namespace std;

int main() {
    int num, ant, pos;
    
    cout << "Digite um número inteiro." << endl;
    cin >> num;
    
    ant = num - 1;
    pos = num + 1;
    
    cout << "O antecessor do número escolhido é... " << ant << "." << endl;
    cout << "O sucessor do número escolhido é... " << pos << "." << endl;

    return 0;
}