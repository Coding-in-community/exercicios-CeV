/*

006 - Dobro, triplo e raiz quadrada
  Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua
  raiz quadrada

*/

#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int numero;
  cin >> numero;

  cout << "O dobro de " << numero << " é " << numero * 2 << "\n";
  cout << "O triplo de " << numero << " é " << numero * 3 << "\n";
  cout << "A raiz quadrada de " << numero << " é " << sqrt(numero) << "\n";

  return 0;
}