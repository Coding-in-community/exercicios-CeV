/*
Desafio 011

Problema: Faça um programa que leia a largura e a altura de uma
          parede em metros, calcule a sua área e a quantidade de
          tinta necessária para pintá-la, sabendo que cada litro
          de tinta pinta uma área de 2 metros quadrados.
*/

fn main() {
    let mut largura = String::new();
    let mut altura = String::new();

    println!("Digite a largura da parede (m): ");
    std::io::stdin().read_line(&mut largura).unwrap();

    println!("Digite a altura da parede (m): ");
    std::io::stdin().read_line(&mut altura).unwrap();

    let largura: f32 = largura.trim().parse().expect("Erro ao ler largura");
    let altura: f32 = altura.trim().parse().expect("Erro ao ler altura");

    let area = largura * altura;
    let qnt_tinta = area / 2.0;

    println!("A área da parede é: {area:.2} m²");
    println!("A quantidade de tinta necessária é: {qnt_tinta:.2} litros");
}
