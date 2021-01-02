/*

012 - Calculando descontos
  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com
  5% de desconto

*/

#include <iostream>

using namespace std;

int main() {
  double preco, desconto;

  cin >> preco;

  desconto = preco * 0.05;

  cout << "O novo preço, com desconto, é de " << preco-desconto << "\n";
  return 0;
}