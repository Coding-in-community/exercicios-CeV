/*

031 - Custo da viagem
	Desenvolva um programa que pergunte a distância de uma viagem em Km.
	Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens
	de até 200km e R$ 0,45 para viagens mais longas

*/

#include <iostream>

using namespace std;

int main() {
	double distancia, preco;

	cin >> distancia;
	if (distancia <= 200) {
		preco = distancia * 0.5;
	} else {
		preco = distancia * 0.45;
	}

	cout << "O preço total é de: " << preco << "\n";
	return 0;
}
