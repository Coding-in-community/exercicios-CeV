/*
Desafio 017

Problema: Faça um programa que leia o comprimento do cateto oposto e
          do cateto adjacente de um triângulo retângulo. Calcule e
          mostre o comprimento da hipotenusa.
*/

fn main() {
    let mut co = String::new();
    let mut ca = String::new();

    println!("Informe o comprimento do cateto oposto: ");
    std::io::stdin().read_line(&mut co).unwrap();

    println!("Informe o comprimento do cateto adjacente: ");
    std::io::stdin().read_line(&mut ca).unwrap();

    let co = co
        .trim()
        .parse::<f32>()
        .expect("Cateto oposto não é um número");

    let ca = ca
        .trim()
        .parse::<f32>()
        .expect("Cateto adjacente não é um número");

    let hipotenusa = co.hypot(ca);

    println!("{}", hipotenusa);
}
