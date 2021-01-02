/*

002 - Respondendo ao usuário
  Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de
  boas-vindas de acordo com o valor digitado

*/

#include <iostream>
#include <string>

using namespace std;

int main() {
  string nome;

  cin >> nome;

  cout << "Seja Bem vindo(a), " << nome << "!\n";

  return 0;
}