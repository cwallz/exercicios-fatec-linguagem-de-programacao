//Exercício da prova 3 
#include <iostream>
using namespace std;

int main (){
    
    int a = 3, b = 0;
    
    while (a > 0){
        b = b + a;
        a--;
    }
    
    cout << b << endl;
    
    return 0;
}