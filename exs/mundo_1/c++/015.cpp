#include <iostream>

using namespace std;

int main() {
  int dias, kms;
  double preco_total;

  cin >> kms >> dias;

  preco_total = (60 * dias) + (0.15 * kms);

  cout << "o total a pagar é de " << preco_total << " reais\n";
  return 0;
}