/*

019 - Sorteando um item na lista
	Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
	Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

using namespace std;

int main() {
	vector<string> lista;
	string temp;

	for (int i=0; i<4; i++) {
		cin >> temp;
		lista.push_back(temp);
	}

	shuffle(lista.begin(), lista.end(), random_device());

	cout << "O escolhido foi " << lista.front() << "\n";
	return 0;
}
