//Exercício 3 - 23/10/2025
//Nome do aluno: Carlos Wallace Pereira
#include <iostream>
#define N 3
using namespace std;

void carregarMatriz(int matriz[3][3]);
void mostraMatriz(int matriz[3][3]);
void verificarRepetidos(int matriz[3][3]);


int main() {
    int matriz[N][N];

    carregarMatriz(matriz);
    mostraMatriz(matriz);
    verificarRepetidos(matriz);
    
    cout << endl << "Tarefa concluída com sucesso!" << endl;

    return 0;
}


void carregarMatriz(int matriz[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << "Digite elemento [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }
}


void mostraMatriz(int matriz[N][N]) {
    cout << "\nMatriz:\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }
}


void verificarRepetidos(int matriz[N][N]) {
    int repetidos[9];  // pode ter no máximo 9 elementos repetidos
    int contRepetidos = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int atual = matriz[i][j];

            // verificar se já está no array de repetidos
            bool jaContado = false;
            for (int k = 0; k < contRepetidos; k++) {
                if (repetidos[k] == atual) {
                    jaContado = true;
                    break;
                }
            }
            if (jaContado) continue;

            // contar quantas vezes aparece na matriz
            int vezes = 0;
            for (int x = 0; x < N; x++) {
                for (int y = 0; y < N; y++) {
                    if (matriz[x][y] == atual) vezes++;
                }
            }

            // se aparecer mais de uma vez, adicionar ao array de repetidos
            if (vezes > 1) {
                repetidos[contRepetidos] = atual;
                contRepetidos++;
            }
        }
    }

    if (contRepetidos == 0) {
        cout << endl <<"Nenhum elemento repetido na matriz." << endl;
    } else {
        cout << endl <<"Quantidade de elementos repetidos: " << contRepetidos << " casos." << endl;
        cout << "Quais são os elementos repetidos: ";
        for (int i = 0; i < contRepetidos; i++) {
            cout << repetidos[i] << " ";
        }
        cout << "." << endl;
    }
}
