/*
Desafio 018

Problema: Faça um programa que leia um ângulo qualquer e mostre na
          tela o valor do seno, cosseno e tangente desse ângulo.
*/

fn main() {
    let mut angulo = String::new();

    println!("Digite um ângulo: ");

    std::io::stdin().read_line(&mut angulo).unwrap();

    let mut angulo: f32 = angulo
        .trim()
        .parse()
        .expect("Valor do ângulo não é um número");

    angulo = angulo * std::f32::consts::PI / 180.0;

    let seno = angulo.sin();
    let cosseno = angulo.cos();
    let tangente = angulo.tan();

    println!("Seno: {}", seno);
    println!("Cosseno: {}", cosseno);
    println!("Tangente: {}", tangente);
}
