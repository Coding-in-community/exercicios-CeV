/*
Desafio 006

Problema: Crie um algoritmo que leia um número e mostre o seu drobro, triplo e raiz
          quadrada.
*/

fn main() {
    let mut number = String::new();

    println!("Insira um número: ");
    std::io::stdin().read_line(&mut number).unwrap();

    let number: i32 = number.trim().parse().unwrap();

    println!("Dobro: {}", number * 2);
    println!("Triplo: {}", number * 3);
    println!("Raiz quadrada: {}", (number as f64).sqrt());
}
