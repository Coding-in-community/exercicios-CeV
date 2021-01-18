/*
Desafio 023

Problema: Faça um programa que leia um número de 0 a 9999 e mostre na tela 
          cada um dos dígitos separados.

Resolução do problema:
*/

using System;

class io {
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
  public static void Main () {
    int num = int.Parse(io.input(
      "Insira um número de 0 a 9999: "
    ));

    int unidade = num / 1 % 10; 
    int dezena = num / 10 % 10;
    int centena = num / 100 % 10;
    int umilhar = num / 1000 % 10;

    io.print($"Unidade: {unidade}");
    io.print($"Dezena: {dezena}");
    io.print($"Centena: {centena}");
    io.print($"Unidade de milhar: {umilhar}");
  }
}