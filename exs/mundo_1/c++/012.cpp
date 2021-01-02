#include <iostream>

using namespace std;

int main() {
  double preco, desconto;

  cin >> preco;

  desconto = preco * 0.05;

  cout << "O novo preço, com desconto, é de " << preco-desconto << "\n";
  return 0;
}