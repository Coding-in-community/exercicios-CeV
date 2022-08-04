/*
Desafio 009

Problema: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua
          tabuada.
*/

fn main() {
    let mut valor = String::new();

    println!("Digite um número: ");
    std::io::stdin().read_line(&mut valor).unwrap();

    let valor: i32 = valor.trim().parse().expect("Erro ao ler valor");

    println!("{} x  1 = {}", valor, valor * 1);
    println!("{} x  2 = {}", valor, valor * 2);
    println!("{} x  3 = {}", valor, valor * 3);
    println!("{} x  4 = {}", valor, valor * 4);
    println!("{} x  5 = {}", valor, valor * 5);
    println!("{} x  6 = {}", valor, valor * 6);
    println!("{} x  7 = {}", valor, valor * 7);
    println!("{} x  8 = {}", valor, valor * 8);
    println!("{} x  9 = {}", valor, valor * 9);
    println!("{} x 10 = {}", valor, valor * 10);
}
