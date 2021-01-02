/*

008 - Conversor de medidas
  Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

*/

#include <iostream>

using namespace std;

int main() {
  double metros, centimetros, milimetros;
  cin >> metros;

  centimetros = (metros * 100);
  milimetros = (metros * 1000);

  cout << metros << " metros é igual a " << centimetros << " centimetros\n";
  cout << metros << " metros é igual a " << milimetros << " milimetros\n";

  return 0;
}