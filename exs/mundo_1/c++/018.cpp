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
