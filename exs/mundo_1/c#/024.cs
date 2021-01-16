/*
Desafio 024

Problema: Crie um programa que leia o nome de uma cidade diga se ela começa ou não 
          com o nome "SANTO".

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
    string cidade = io.input("Digite o nome de cidade: ");

    bool hasSanto = cidade
      .ToLower()
      .StartsWith("santo");

    io.print($"O nome da cidade digitada começa com \"SANTO\": {hasSanto}");
  }
}