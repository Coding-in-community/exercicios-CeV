/*

011 - Pintando parede
  Faça um programa que leia a largura e a algura de uma parede em metros,
  calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
  que cada litro de tinta pinta uma área de 2m²

*/

#include <iostream>

using namespace std;

int main() {
  double altura, largura, area, litros;

  cin >> largura >> altura;

  area = largura * altura;
  litros = area/2;

  cout << "Necessita de " << litros << "L para pintar a parede de area " << area << "m²\n";

  return 0;
}