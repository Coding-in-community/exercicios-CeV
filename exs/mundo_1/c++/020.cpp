/*

020 - Sorteando uma ordem na lista
	O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
	Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

using namespace std;

void repr(vector<string> lista) {
	for (int i=0;i<4;i++) {
		cout << lista.at(i) << "\n";
	}
}

int main() {
	vector<string> lista;
	string temp;

	for (int i=0; i<4; i++) {
		cin >> temp;
		lista.push_back(temp);
	}

	shuffle(lista.begin(), lista.end(), random_device());

	cout << "A ordem é a seguinte:\n";
	repr(lista);
	return 0;
}
