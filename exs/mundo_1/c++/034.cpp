/*

034 - Aumentos múltiplos
	Escreva um programa que pergunte o salário de um funcionário e
	calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de R$ 15%

*/

#include <iostream>

using namespace std;

int main() {
	double salario, aumento;

	cin >> salario;
	if (salario > 1250) {
		aumento = salario * 0.1;
	} else {
		aumento = salario * 0.15;
	}

	cout << "o aumento será de: " << aumento << "\n";
	return 0;
}
