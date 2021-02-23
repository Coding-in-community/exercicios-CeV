/*

032 - Ano bissexto
	Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

*/

#include <iostream>

using namespace std;

int main() {
	int ano;

	cin >> ano;
	if (ano % 4 == 0 &&
			ano % 100 != 0 ||
			ano % 400 == 0) {
		cout << "É Bissexto\n";
	} else {
		cout << "Não é Bissexto\n";
	}

	return 0;
}
