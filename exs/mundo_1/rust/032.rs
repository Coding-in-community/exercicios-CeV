/*
Desafio 032

Problema: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
*/

fn main() {
    let mut ano = String::new();

    println!("Insira um ano");
    std::io::stdin().read_line(&mut ano).unwrap();

    let ano = ano
        .trim()
        .parse::<i32>()
        .expect("Valor inserido não é um número válido.");

    if (ano % 4 == 0) && ((ano % 100 != 0) || (ano % 400 == 0)) {
        return println!("O ano de {ano} é bissexto");
    }

    println!("O ano de {ano} não é bissexto")
}
