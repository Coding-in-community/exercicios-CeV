/*
Desafio 034

Problema: Escreva um programa que pergunte o salário de um funcionário
          e calcule o valor do seu aumento. Para salários superiores a
          R$1250,00, calcule um aumento de 10%. Para os inferiores ou
          iguais, o aumento é de 15%.
*/

fn main() {
    let mut salario_original = String::new();

    println!("Informe seu salário em Real:");
    std::io::stdin().read_line(&mut salario_original).unwrap();

    salario_original = salario_original
        .trim()
        .parse::<f32>()
        .expect("O valor não é um número");

    let salario_aumentado: f32;

    if salario_original <= 1250.00 {
        salario_aumentado = salario_original * 1.15;
    } else {
        salario_aumentado = salario_original * 1.10;
    }

    println!("O salário com aumento é: R${salario_aumentado:.2}");
}
