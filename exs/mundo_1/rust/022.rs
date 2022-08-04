/*
Desafio 022

Problema: Crie um programa que leia o nome completo de uma pessoa
          e mostre:
              - O nome com todas as letras maiúsculas e minúsculas.
              - Quantas letras ao todo(sem considerar espaços)
              - Quantas letras tem o primeiro nome.
*/

fn main() {
    let mut input = String::new();

    println!("Digite o nome completo: ");
    std::io::stdin().read_line(&mut input).unwrap();

    input = input.trim().to_string();

    let minusculo = input.to_lowercase();
    let maiusculo = input.to_uppercase();
    let contador_letras = input.replace(" ", "").len();
    let primeiro_nome = input.split(" ").nth(0).unwrap();

    println!("Nome completo: {}", maiusculo);
    println!("Nome completo: {}", minusculo);
    println!("Quantidade de letras: {}", contador_letras);
    println!("Quantidade de letras do primeiro nome: {}", primeiro_nome);
}
