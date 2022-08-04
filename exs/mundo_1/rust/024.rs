/*
Desafio 024

Problema: Crie um programa que leia o nome de uma cidade diga se ela começa ou não
          com o nome "SANTO".
*/

fn main() {
    let mut input = String::new();

    println!("Digite o nome da cidade: ");
    std::io::stdin().read_line(&mut input).unwrap();

    let inicia_com_santo = input.trim().to_uppercase().starts_with("SANTO");

    println!("O nome da cidade digitada começa com \"SANTO\": {inicia_com_santo}");
}
