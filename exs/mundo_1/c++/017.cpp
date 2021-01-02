/*

017 - Catetos e hipotenusa
  Faça um programa que leia o comprimento do cateto oposto (co) e do cateto
  adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da
  hipotenusa

*/

#include <iostream>
#include <cmath>

using namespace std;

int main() {
  double cateto_oposto, cateto_adjacente, hipotenusa;

  cin >> cateto_oposto >> cateto_adjacente;
  hipotenusa = pow(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2), 0.5);

  cout << "A Hipotenusa é igual a " << hipotenusa << "\n";
  return 0;
}