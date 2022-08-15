/*
Desafio 035

Problema: Desenvolva um programa que leia o comprimento de três
          retas e diga ao usuário se elas podem ou não formar um triângulo
*/

fn main() {
    let mut lado_a = String::new();
    let mut lado_b = String::new();
    let mut lado_c = String::new();

    println!("Informe a medida do lado A: ");
    std::io::stdin().read_line(&mut lado_a).unwrap();

    println!("Informe a medida do lado B: ");
    std::io::stdin().read_line(&mut lado_b).unwrap();

    println!("Informe a medida do lado C: ");
    std::io::stdin().read_line(&mut lado_c).unwrap();

    let lado_a = lado_a
        .trim()
        .parse::<i32>()
        .expect("Valor inserido não é um número válido.");

    let lado_b = lado_b
        .trim()
        .parse::<i32>()
        .expect("Valor inserido não é um número válido.");

    let lado_c = lado_c
        .trim()
        .parse::<i32>()
        .expect("Valor inserido não é um número válido.");

    let diff_ab = (lado_a - lado_b).abs();
    let diff_bc = (lado_a - lado_c).abs();
    let diff_ca = (lado_a - lado_c).abs();

    let sum_ab = lado_a + lado_b;
    let sum_bc = lado_a + lado_c;
    let sum_ca = lado_a + lado_c;

    let is_a_valid = diff_bc < lado_a && lado_a < sum_bc;
    let is_b_valid = diff_ca < lado_b && lado_b < sum_ca;
    let is_c_valid = diff_ab < lado_c && lado_c < sum_ab;

    if is_a_valid && is_b_valid && is_c_valid {
        return println!("As retas PODEM formar um triângulo.");
    }

    return println!("As retas NÂO podem formar um triângulo.");
}
