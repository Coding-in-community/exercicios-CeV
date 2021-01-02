/*

003 - Somando dois números
  Crie um script Python que leia dois números e tente mostrar a soma entre eles

*/

#include <iostream>

using namespace std;

int main() {
  int N1, N2, sum;
  cin >> N1 >> N2;

  sum = (N1 + N2);

  cout << "A soma é igual a " << sum << "\n";

  return 0;
}