/*
Desafio 010

Problema: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
          mostre quantos dólares ela pode comprar.
*/

fn main() {
    const DOLAR: f32 = 3.27;
    const EURO: f32 = 3.96;

    let mut valor = String::new();

    println!("Digite um número: ");
    std::io::stdin().read_line(&mut valor).unwrap();

    let valor: f32 = valor.trim().parse().expect("Erro ao ler valor");

    let conversao_dolar = valor / DOLAR;
    let conversao_euro = valor / EURO;

    println!("Com R$ {valor:.2} você pode comprar ${conversao_dolar:.2}");
    println!("Com a mesma quantidade você pode comprar €{conversao_euro:.2}");
}
