/*
Desafio 012

Problema: Faça um algoritmo que leia o preço de um produto e 
          mostre seu novo preço, com 5% de desconto

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
        double preco = double.Parse(
          io.input("Informe o preço do produto: R$")
        );

        double total = Math.Truncate((preco * 0.95 * 100)) / 100;

        io.print($"Total à pagar com 5% de desconto: R${total}");
    }
}