/*
Desafio 028

Problema: Escreva um programa que faça o computador "pensar"
          em um número inteiro entre 0 e 5 e peça para o usuário
          tentar descobrir qual foi o número escolhido pelo computador.
          O programa deverá escrever na tela se o usuário venceu ou perdeu.
*/

use rand::Rng;

fn main() {
    let mut input = String::new();

    println!("Insira um número: ");
    std::io::stdin().read_line(&mut input).unwrap();

    let input = input.trim().parse::<u8>().expect("Não é um número");

    let mut rng = rand::thread_rng();
    let randint = rng.gen_range(0..6) as u8;

    if input == randint {
        return println!("Você acertou!");
    }

    return println!("Você errou!");
}
