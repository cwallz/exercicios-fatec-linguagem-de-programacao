//Exercício 1 - 23/10/2025
//Nome do aluno: Carlos Wallace Pereira
#include <iostream>
#define N 3
using namespace std;

void carregarMatriz (int matriz[][3], int linhas, int colunas);
void mostraMatriz (int matriz[][3], int linhas, int colunas);
void somarMatrizes(int a[][3], int b[][3], int c[][3], int linhas, int colunas);

int main() {
    int a[N][N], b[N][N], c[N][N]; 

    cout << "Digite os elementos da primeira matriz " << N << "X" << N << endl;
    
    carregarMatriz (a, N, N);
    mostraMatriz (a, N, N);
    
    cout << endl << "Digite os elementos da segunda matriz " << N << "X" << N << endl;
   
    carregarMatriz (b, N, N);
    mostraMatriz (b, N, N);
    
    somarMatrizes(a, b, c, N, N);
    
    cout << endl << "A soma da matriz primeira e segunda matriz é:" << endl;
    
    mostraMatriz(c, N, N);

    cout << endl << "Tarefa concluída com sucesso!" << endl;
    
    return 0;
}

void carregarMatriz (int matriz[][3], int linhas, int colunas){
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }
}

void mostraMatriz (int matriz[][3], int linhas, int colunas){
    cout << endl << "Matriz Carregada:" << endl;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }
}

void somarMatrizes(int a[][3], int b[][3], int c[][3], int linhas, int colunas) {
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            c[i][j] = a[i][j] + b[i][j];
        }
    }
}
