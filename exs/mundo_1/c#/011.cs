/*
Desafio 011

Problema: Faça um programa que leia a largura e a algura de uma parede em metros, 
          calcule a sua área e a quantidade de tinta necessária para pintá-la, 
          sabendo que cada litro de tinta pinta uma área de 2m²

Resolução do problema:
*/

using System;

static class io {
    public static string input(string text) {
        Console.Write(text);
        return Console.ReadLine();
    }
    
    public static void print(object data, string end="\n") {
        string text = data.ToString();

        Console.Write($"{text}{end}");
    }
}

class Program {
    public static void Main() {
        double largura = double.Parse(
          io.input("Informe a largura da parede: ")
        );
        double altura = double.Parse(
          io.input("Informe a altura da parede: ")
        );

        double area = largura*altura;
        double qtndTinta = area / 2;

        io.print($"A parede tem uma área de {area}m²");
        io.print($"Será necessário {qtndTinta}L de tinta para pintar a parede");
    }
}