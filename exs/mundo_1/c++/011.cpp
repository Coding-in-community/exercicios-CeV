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