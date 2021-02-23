/*

029 - Radar eletrônico
	Escreva um programa que leia a velocidade de um carro.
	Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
	foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

*/

#include <iostream>

using namespace std;

int main() {
	double velocidade, multa;

	cin >> velocidade;
	if (velocidade > 80) {
		cout << "Você foi multado em " << (velocidade - 80) * 7 << " reais\n";
	} else {
		cout << "Você não foi multado\n";
	}

	return 0;
}
