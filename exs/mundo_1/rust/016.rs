/*
Desafio 016

Problema: Crie um programa que leia um número Real qualquer
          pelo teclado e mostre na tela a sua porção Inteira.
*/

fn main() {
    let mut valor = String::new();

    std::io::stdin().read_line(&mut valor).unwrap();

    let valor = valor
        .trim()
        .parse::<f32>()
        .expect("O valor não é um número");

    println!("{}", valor as i32);
}
