/*
Desafio 023

Problema: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
          um dos dígitos separados.
*/

fn main() {
    let mut input = String::new();

    println!("Digite um número entre  0 e 9999: ");
    std::io::stdin().read_line(&mut input).unwrap();

    let input = input.trim().parse::<f32>().expect("Valor não é um número");

    if 0.0 <= input && input < 10000.0 {
        let uni = (input / 1.0).floor() % 10.0;
        let dez = (input / 10.0).floor() % 10.0;
        let cen = (input / 100.0).floor() % 10.0;
        let mil = (input / 1000.0).floor() % 10.0;

        println!("Unidade: {}", uni);
        println!("Dezena: {}", dez);
        println!("Centena: {}", cen);
        println!("Milhar: {}", mil);
    } else {
        println!("Número inválido");
    }
}
