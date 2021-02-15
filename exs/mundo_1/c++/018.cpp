/*

018 - Seno, cosseno e tangente
	Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

*/

#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int angulo;
	double sen, coss, tang;

	cin >> angulo;

	sen = sin(angulo);
	coss = cos(angulo);
	tang = tan(angulo);

	cout << "Dado o ângulo " << angulo << ":\n";
	cout << "O Seno é: " << sen << "\n";
	cout << "O Cosseno é: " << coss << "\n";
	cout << "A tangente é: " << tang << "\n";
	return 0;
}
