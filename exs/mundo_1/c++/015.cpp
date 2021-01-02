/*

015 - Aluguel de carros
  Escreva um programa que pergunte a quantidade de Km percorridos por um carro
  alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
  pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

*/

#include <iostream>

using namespace std;

int main() {
  int dias, kms;
  double preco_total;

  cin >> kms >> dias;

  preco_total = (60 * dias) + (0.15 * kms);

  cout << "o total a pagar é de " << preco_total << " reais\n";
  return 0;
}