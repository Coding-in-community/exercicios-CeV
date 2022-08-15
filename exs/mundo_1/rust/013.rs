/*
Desafio 013

Problema: Faça um algoritmo que leia o salário de um funcionário
          e mostre seu novo salário, com 15% de aumento.
*/

fn main() {
    let mut salario = String::new();

    println!("Informe seu sálario (R$):");
    std::io::stdin().read_line(&mut salario).unwrap();

    let salario: f32 = salario.trim().parse().expect("Erro ao ler sálario");

    let salario_aumentado = salario * 1.15;

    println!("Salário final: R${salario_aumentado:.2}");
}
