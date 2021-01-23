/*
Desafio 016

Problema: Crie um programa que leia um número real qualquer 
          pelo teclado e mostre na tela a sua porção inteira

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
        double num = double.Parse(
          io.input("Informe um número flutuante: ")
        );

        io.print(Math.Truncate(num));
    }
}