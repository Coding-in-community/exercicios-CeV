/*
Desafio 031

Problema: Desenvolva um programa que pergunte a distância de
          uma viagem em Km. Calcule o preço da passagem, cobrando
          R$0,50 por Km para viagens de até 200Km e R$0,45 para
          viagens mais longas.
*/

fn main() {
    let mut input = String::new();

    println!("Informe a distância em KM: ");
    std::io::stdin().read_line(&mut input).unwrap();

    let input = input.trim().parse::<f32>().expect("Input is not an number");

    let preco_passagem = if input > 200.0 {
        input * 0.45
    } else {
        input * 0.5
    };

    println!("O valor da passagem será R${:.2}", preco_passagem);
}
