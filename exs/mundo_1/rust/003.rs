/*
Desafio 003

Problema: Crie um script Python que leia dois números e tente mostrar a soma entre
          eles
*/

fn main() {
    let mut number1 = String::new();
    let mut number2 = String::new();

    println!("Digite o primeiro número: ");
    std::io::stdin().read_line(&mut number1).unwrap();

    println!("Digite o segundo número: ");
    std::io::stdin().read_line(&mut number2).unwrap();

    let number1 = number1
        .trim()
        .parse::<i32>()
        .expect("Valor inserido não é um número");

    let number2 = number2
        .trim()
        .parse::<i32>()
        .expect("Valor inserido não é um número");

    let sum = number1 + number2;

    println!("A soma entre {number1} e {number2} vale {sum}");
}
