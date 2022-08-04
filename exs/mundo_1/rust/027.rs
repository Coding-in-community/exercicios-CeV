/*
Desafio 027

Problema: Faça um programa que leia o nome completo de uma
          pessoa, mostrando em seguida o primeiro e o último
          nome separadamente.
*/

fn main() {
    let mut input = String::new();

    println!("Informe seu nome: ");
    std::io::stdin().read_line(&mut input).unwrap();

    input = input.trim().to_lowercase();

    let first_name = input.split(" ").nth(0).expect("O nome não foi inserido");
    let last_name = input.split(" ").last().unwrap();

    println!("Primeiro: {} \nUltimo: {}", first_name, last_name);
}
