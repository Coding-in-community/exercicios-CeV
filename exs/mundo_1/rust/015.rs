/*
Desafio 015

Problema: Escreva um programa que pergunte a quantidade de Km
          percorridos por um carro alugado e a quantidade de dias
          pelos quais ele foi alugado. Calcule o preço a pagar,
          sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
*/

fn main() {
    let mut kms = String::new();
    let mut dias = String::new();

    println!("Informe a quantidade de Km percorridos: ");
    std::io::stdin().read_line(&mut kms).unwrap();

    println!("Informe a quantidade de dias alugado: ");
    std::io::stdin().read_line(&mut dias).unwrap();

    let kms = kms.trim().parse::<f32>().expect("O valor não é um número");
    let dias = dias.trim().parse::<f32>().expect("O valor não é um número");

    let valor_km = kms * 0.15;
    let valor_dia = dias * 60.0;
    let valor_total = valor_km + valor_dia;

    println!("O valor total a pagar é: R${valor_total:.2}");
}
