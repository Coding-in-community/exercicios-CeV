/*
Desafio 030

Problema: Crie um programa que leia um número inteiro e mostre na tela se ele é
          PAR ou ÍMPAR.
*/

fn main() {
    let mut input = String::new();

    println!("informe um número: ");
    std::io::stdin().read_line(&mut input).unwrap();

    let input = input.trim().parse::<i64>().expect("Não é um número");

    println!(
        "O número {input} é {}",
        if input % 2 == 0 { "par" } else { "impar" }
    );
}
