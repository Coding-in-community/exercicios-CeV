/*
Desafio 015

Problema: Escreva um programa que pergunte a quantidade de Km percorridos por um 
          carro alugado e a quantidade de dias pelos quais ele foi alugado. 
          Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

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
        int dia = int.Parse(
          io.input("Dias alugado: ")
        );

        double km = double.Parse(
          io.input("Km rodados: ")
        );

        double valor = (dia * 60) + (km * 0.15);
        double valorTruncado = Math.Truncate((valor * 100)) / 100;

        io.print($"Total a pagar R${valorTruncado}");
    }
}