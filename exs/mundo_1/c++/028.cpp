/*

	028 - Jogo da Adivinhação v1.0
	Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
	tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

*/

#include <iostream>
#include <time.h>
#include <stdlib.h>

using namespace std;

int main() {
	int chute, numero;

	cin >> chute;

	srand(time(NULL));
	numero = rand() % 4 + 1;

	if (chute == numero) {
		cout << "Você venceu!\n";
	} else {
		cout << "Você perdeu\n";
	}
	return 0;
}
