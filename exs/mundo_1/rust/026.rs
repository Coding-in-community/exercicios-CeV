/*
Desafio 026

Problema: Faça um programa que leia uma frase pelo teclado
          e mostre quantas vezes aparece a letra "A", em que
          posição ela aparece a primeira vez e em que posição
          ela aparece a última vez.
*/

fn main() {
    let mut input = String::new();

    println!("Digite uma frase: ");
    std::io::stdin().read_line(&mut input).unwrap();

    input = input.trim().to_lowercase();

    let count_a = input.chars().filter(|char| *char == 'a').count();
    let first_a = input.find('a').unwrap() as i32 + 1;
    let last_a = input.rfind('a').unwrap() as i32 + 1;

    println!("Quantas vezes a letra \"A\" apareceu: {}", count_a);
    println!("Ela aparece a primeira vez na posição: {}", first_a);
    println!("Ela aparece a ultima vez na posição: {}", last_a);
}
