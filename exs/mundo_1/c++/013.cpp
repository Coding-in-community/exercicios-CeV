/*

013 - Reajuste salarial
  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
  salário, com 15% de aumento

*/

#include <iostream>

using namespace std;

int main() {
  double salario, ajuste;

  cin >> salario;

  ajuste = salario + (salario * 0.15);

  cout << "seu novo salário é de " << ajuste << " reais\n";
  return 0;
}