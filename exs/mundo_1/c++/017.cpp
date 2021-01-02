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