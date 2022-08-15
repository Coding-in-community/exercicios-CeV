/*
Desafio 005

Problema: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor
          e seu antecessor
*/

fn main() {
    let mut input = String::new();

    println!("Digite um número: ");
    std::io::stdin()
        .read_line(&mut input)
        .expect("Falha ao ler o input");

    let result = input
        .trim()
        .to_string()
        .parse::<i32>()
        .expect("Não é um número");

    let next = result + 1;
    let previous = result - 1;

    println!("O sucessor de {input} é {next} e o antecessor é {previous}");
}
