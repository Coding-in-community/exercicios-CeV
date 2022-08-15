/*
Desafio 019

Problema: Um professor quer sortear um dos seus quatro alunos para
          apagar o quadro. Faça um programa que ajude ele, lendo o
          nome dos alunos e escrevendo na tela o nome do escolhido.
*/

/*
AVISO: Rand não é uma biblioteca padrão do Rust, é necessário a
utilização do Cargo para sua instalação e execução.
*/

use rand::Rng;

fn main() {
    let mut names = Vec::new();

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

    names.push(aluno1);
    names.push(aluno2);
    names.push(aluno3);
    names.push(aluno4);

    let mut rng = rand::thread_rng();
    let index = rng.gen_range(0..names.len());

    println!("O aluno escolhido foi {}", names[index]);
}
