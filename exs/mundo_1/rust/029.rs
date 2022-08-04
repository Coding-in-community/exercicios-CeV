/*
Desafio 029

Problema: Escreva um programa que leia a velocidade de um carro.
          Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
          que ele foi multado. A multa vai custar R$7,00 por cada
          Km acima do limite.
*/

fn main() {
    let mut velocidade = String::new();

    println!("Velocidade: ");
    std::io::stdin().read_line(&mut velocidade).unwrap();

    let velocidade = velocidade.trim().parse::<u16>().expect("Não é um número");

    if velocidade > (80 as u16) {
        println!("Você foi multado");
        let multa = ((velocidade - 80) * 7) as f32;
        println!("Você vai pagar R$ {multa:.2} de multa.")
    }
}
