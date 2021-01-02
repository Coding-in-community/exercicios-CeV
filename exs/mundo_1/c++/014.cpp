/*

014 - Conversor de temperaturas
  Conversor de temperaturas: escreva um programa que converta uma temperatura
  digitada em ºC para ºF

*/

#include <iostream>

using namespace std;

int main() {
  double tempC, tempF;

  cin >> tempC;

  tempF = (tempC * 9/5) + 32;

  cout << tempC << "ºC em fahrenheit é " << tempF << "ºF\n";
  return 0;
}