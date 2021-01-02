/*

005 - Antecessor e sucessor
  Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e
  seu antecessor

*/

#include <iostream>

using namespace std;

int main() {
  int numero, antecessor, sucessor;
  cin >> numero;

  antecessor = numero - 1;
  sucessor = numero + 1;

  cout << "O antecessor de " << numero << " é " << antecessor << "\n";
  cout << "O sucessor de " << numero << " é " << sucessor << "\n";


  return 0;
}