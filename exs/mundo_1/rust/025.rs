/*
Desafio 025

Problema: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"
          no nome.
*/

fn main() {
    let mut input = String::new();

    println!("Digite o nome da cidade: ");
    std::io::stdin().read_line(&mut input).unwrap();

    input = input.trim().to_string();

    let tem_silva = input.to_uppercase().contains("SILVA");

    println!("O nome da pessoa digitada tem \"SILVA\": {tem_silva}",);
}
