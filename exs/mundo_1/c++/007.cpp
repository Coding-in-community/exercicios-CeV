/*

007 - Média aritmética
  Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a
  sua média

*/

#include <iostream>

using namespace std;

int main() {
  float nota1, nota2, media;
  cin >> nota1 >> nota2;

  media = (nota1 + nota2)/2;

  cout << "A média entre as duas nota é " << media << "\n";

  return 0;
}