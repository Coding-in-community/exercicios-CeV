/*
Desafio 012

Problema: Faça um algoritmo que leia o preço de um produto e
          mostre seu novo preço, com 5% de desconto.
*/

fn main() {
    let mut valor = String::new();

    println!("Informe o preço do produto (R$):");
    std::io::stdin().read_line(&mut valor).unwrap();

    let valor: f32 = valor.trim().parse().expect("Erro ao ler valor");

    let valor_desconto = valor * 0.95;

    println!("O valor do produto com desconto é: R${valor_desconto:.2}");
}
