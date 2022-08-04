/*
Desafio 020

Problema: O mesmo professor do desafio 019 quer sortear a ordem
          de apresentação de trabalhos dos alunos. Faça um programa
          que leia o nome dos quatro alunos e mostre a ordem sorteada.
*/

use rand::prelude::SliceRandom;

fn main() {
    let mut alunos = Vec::new();

    let mut aluno1 = String::new();
    let mut aluno2 = String::new();
    let mut aluno3 = String::new();
    let mut aluno4 = String::new();

    println!("Digite o nome do aluno 1: ");
    std::io::stdin().read_line(&mut aluno1).unwrap();

    println!("Digite o nome do aluno 2: ");
    std::io::stdin().read_line(&mut aluno2).unwrap();

    println!("Digite o nome do aluno 3: ");
    std::io::stdin().read_line(&mut aluno3).unwrap();

    println!("Digite o nome do aluno 4: ");
    std::io::stdin().read_line(&mut aluno4).unwrap();

    alunos.push(aluno1.trim());
    alunos.push(aluno2.trim());
    alunos.push(aluno3.trim());
    alunos.push(aluno4.trim());

    alunos.shuffle(&mut rand::thread_rng());

    println!("A ordem de apresentação será: {:?}", alunos);
}
