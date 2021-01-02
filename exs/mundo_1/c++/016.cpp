/*

016 - Quebrando um número
  Crie um programa que leia um número real qualquer pelo teclado e mostre na
  tela a sua porção inteira

*/

#include <iostream>

using namespace std;

int main() {
  double numero_real;

  cin >> numero_real;
  cout << (int) numero_real << "\n";

  return 0;
}