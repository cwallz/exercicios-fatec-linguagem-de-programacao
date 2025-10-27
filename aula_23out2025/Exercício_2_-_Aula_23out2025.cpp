//Exercício 2 - 23/10/2025
//Nome do aluno: Carlos Wallace Pereira
#include <iostream>
#define MAX 100
using namespace std;

void carregarMatriz (int a[][MAX], int linhas, int colunas);
void mostraMatriz (int a[][MAX], int linhas, int colunas);

int main() {
    int M, N;
    int matriz[MAX][MAX];

    do {
        cout << "Digite o número de linhas da matriz: " << endl;
        cin >> M;
        if (M <= 0){
            cout << "Número inválido" << endl;
        }
    } while (M <= 0);
    
    do {
        cout << "Digite o número de colunas da matriz: " << endl;
        cin >> N;
        if (N<= 0){
            cout << "Número inválido" << endl;
        }
    } while (N <= 0);

    carregarMatriz (matriz, M, N);
    mostraMatriz (matriz, M, N);


    cout << endl << "Tarefa concluída com sucesso!" << endl;
    
    return 0;
}


void carregarMatriz (int a[][MAX], int linhas, int colunas){
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            if (i == j)
                a[i][j] = 0;
            else if (i > j)
                a[i][j] = i;
            else // i < j
                a[i][j] = j;
        }
    }    
}

void mostraMatriz (int a[][MAX], int linhas, int colunas){
    cout << endl << "Matriz gerada:" << endl;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            cout << a[i][j] << "\t";
        }
        cout << endl;
    }
}