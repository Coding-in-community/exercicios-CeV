/*
Desafio 014

Problema: Escreva um programa que converta uma temperatura
          digitando em graus Celsius e converta para graus Fahrenheit.
*/

fn main() {
    let mut input = String::new();

    println!("Digite a temperatura em Celsius: ");
    std::io::stdin().read_line(&mut input).unwrap();

    let celsius: f32 = input.trim().parse().expect("Erro ao ler valor");

    let fahrenheit = (celsius * 9.0 / 5.0) + 32.0;

    println!("{celsius:.1}°C é igual a {fahrenheit:.1}°F");
}
