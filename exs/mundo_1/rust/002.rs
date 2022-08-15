/*
Desafio 002

Problema: Crie um script que leia o nome de uma pessoa e mostre uma mensagem de
          boas-vindas de acordo com o valor digitado
*/

fn main() {
    let mut name = String::new();

    println!("Digite seu nome: ");
    std::io::stdin()
        .read_line(&mut name)
        .expect("Falha ao ler o nome");

    println!("Olá, {name}");
}
