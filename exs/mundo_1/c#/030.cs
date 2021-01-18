/*
Desafio 030

Problema:  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

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
      "Insira um número: "
    ));

    if (num % 2 == 0) {
      io.print("O número é PAR");
    }

    else {
      io.print("O número é ÍMPAR");
    }
  }
}