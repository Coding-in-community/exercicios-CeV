/*

033 - Maior e menor valores
	Faça um programa que leia três números e mostre qual é o maior e qual é o menor

*/

#include <iostream>

using namespace std;

int main() {
	int temp, maior, menor;

	for (int i=0; i<3; i++) {
		cin >> temp;

		if (i == 0) {
			maior = menor = temp;
		} else if (temp < menor) {
			menor = temp;
		} else if (temp > maior) {
			maior = temp;
		}
	}

	cout << "O maior é: " << maior << "\n";
	cout << "O menor é: " << menor << "\n";
	return 0;
}
