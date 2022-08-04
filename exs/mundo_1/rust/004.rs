/*
Desafio 004

Problema: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
          primitivo e todas as informações possíveis sobre ele
*/

fn main() {
    let mut input = String::new();

    println!("Digite algo: ");
    std::io::stdin()
        .read_line(&mut input)
        .expect("Falha ao ler o input");

    input = input.trim().to_string();

    let char_count = input.chars().count();
    let is_number = input.chars().all(|c| c.is_numeric());
    let is_alphabet = input.chars().all(|c| c.is_alphabetic());
    let is_alphanum = input.chars().all(|c| c.is_alphanumeric());
    let is_float = input.parse::<f32>().is_ok();
    let is_lowercase = is_alphabet && input.to_lowercase() == input;
    let is_uppercase = is_alphabet && input.to_uppercase() == input;
    let is_whitespace = input.chars().all(|c| c.is_whitespace());
    let is_capitalized = input.chars().nth(0).unwrap().is_uppercase();

    println!("Você digitou {} caracteres", char_count);
    println!("É letrao? {}", is_alphabet);
    println!("É número? {}", is_number);
    println!("É float?: {}", is_float);
    println!("É alfanumérico? {}", is_alphanum);
    println!("É apenas espaço em branco? {}", is_whitespace);
    println!("É letra minúscula? {}", is_lowercase);
    println!("É letra maiúscula? {}", is_uppercase);
    println!("Está capitalizada? {}", is_capitalized);
}
