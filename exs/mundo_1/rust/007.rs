/*
Desafio 007

Problema: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre
          a sua média.
*/

fn main() {
    let mut nota1 = String::new();
    let mut nota2 = String::new();

    println!("Digite a primeira nota: ");
    std::io::stdin().read_line(&mut nota1).unwrap();

    println!("Digite a segunda nota: ");
    std::io::stdin().read_line(&mut nota2).unwrap();

    let nota1 = nota1.trim().parse::<f32>().expect("Erro ao ler nota 1");
    let nota2 = nota2.trim().parse::<f32>().expect("Erro ao ler nota 2");

    let media = (nota1 + nota2) / 2.0;

    println!("A média é: {:.1}", media);
}
