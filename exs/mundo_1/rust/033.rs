/*
Desafio 033

Problema: Faça um programa que leia três números e mostre qual é o maior e qual é
          o menor.
*/

fn main() {
    let mut num1 = String::new();
    let mut num2 = String::new();
    let mut num3 = String::new();

    println!("Informe o primeiro número");
    std::io::stdin().read_line(&mut num1).unwrap();

    println!("Informe o segundo número");
    std::io::stdin().read_line(&mut num2).unwrap();

    println!("Informe o terceiro número");
    std::io::stdin().read_line(&mut num3).unwrap();

    let num1 = num1
        .trim()
        .parse::<i32>()
        .expect("Valor inserido não é um número válido.");

    let num2 = num2
        .trim()
        .parse::<i32>()
        .expect("Valor inserido não é um número válido.");

    let num3 = num3
        .trim()
        .parse::<i32>()
        .expect("Valor inserido não é um número válido.");

    let mut menor = num1;
    let mut maior = num1;

    if num2 > num1 && num2 > num3 {
        maior = num2
    }

    if num3 > num1 && num3 > num2 {
        maior = num3
    }

    if num2 < num1 && num2 < num3 {
        menor = num2
    }

    if num3 < num1 && num3 < num2 {
        menor = num3
    }

    println!("O número {maior} é o MAIOR");
    println!("O número {menor} é o MENOR");
}
