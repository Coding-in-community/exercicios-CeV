/*

023 - Separando dígitos de um número
	Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

*/

#include <iostream>

using namespace std;

int main() {
	int n, unidade, dezena, centena, milhar;

	cin >> n;
	unidade = n % 10;
	dezena = n / 10 % 10;
	centena = n / 100 % 10;
	milhar = n / 1000 % 10;

	cout << "Unidade: " << unidade << "\n";
	cout << "Dezena: " << dezena << "\n";
	cout << "Centena: " << centena << "\n";
	cout << "Milhar: " << milhar << "\n";
	return 0;
}
