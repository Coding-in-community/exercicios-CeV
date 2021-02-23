/*
035 - Analisando triângulo v1.0
	Desenvolva um programa que leia o comprimento de três retas e diga
	ao usuário se elas podem ou não formar um triângulo
*/

#include <iostream>

using namespace std;

int main() {
	double r1, r2, r3;

	cin >> r1 >> r2 >> r3;

	if ((r2+r3) > r1 &&
			(r1+r3) > r2 &&
			(r1+r2) > r3) {
		cout << "Forma um triângulo\n";
	} else {
		cout << "Não forma um triângulo\n";
	}
	return 0;
}
