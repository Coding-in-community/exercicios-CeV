#include <iostream>
#include <string>

using namespace std;

int main() {
	string cidade, inicio;

	cin >> cidade;
	inicio = cidade.substr(0, 5);

	if (inicio == "Santo") {
		cout << "Começa com 'Santo'\n";
	} else {
		cout << "Não começa com 'Santo'\n";
	}
	return 0;
}
