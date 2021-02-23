/*

030 - Par ou ímpar?
	Crie um programa que leia um número inteiro e
	mostre na tela se ele é PAR ou ÍMPAR

*/

#include <iostream>

using namespace std;

int main() {
	int n;

	cin >> n;
	if (n % 2 == 0) {
		cout << "É par\n";
	} else {
		cout << "É impar\n";
	}

	return 0;
}
