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
