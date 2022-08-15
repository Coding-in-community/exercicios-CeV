/*
Desafio 008

Problema: Escreva um programa que leia um valor em metros e o exiba convertido em
          centímetros e milímetros.
*/

fn main() {
    let mut metro = String::new();

    println!("Digite um valor em metros: ");
    std::io::stdin().read_line(&mut metro).unwrap();

    let m: f32 = metro.trim().parse().expect("Erro ao ler valor");

    let dc = metro * 10.0;
    let cm = metro * 100.0;
    let mm = metro * 1000.0;

    println!("{m} metros é igual a {dm} decametros, {cm} centímetros e {mm} milímetros",);
}
