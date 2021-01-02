/*

010 - Conversor de moedas
  Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
  quantos dólares ela pode comprar

*/

#include <iostream>

using namespace std;

int main() {
  double dinheiro, dolar;
  cin >> dinheiro;

  dolar = dinheiro * 5.12;

  cout << "Está quantia vale " << dolar << " dolares!\n";

  return 0;
}