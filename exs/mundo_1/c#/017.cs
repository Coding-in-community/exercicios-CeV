/*
Desafio 017

Problema: Faça um programa que leia o comprimento do cateto oposto (co) e 
          do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre 
          o comprimento da hipotenusa

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
        double oposto = double.Parse(
          io.input("Informe o cateto oposto: ")
        );

        double adjacente = double.Parse(
          io.input("Informe o cateto adjacente: ")
        );

        double hipotenusa = Math.Sqrt(
          Math.Pow(oposto, 2) + Math.Pow(adjacente, 2)
        );

        io.print($"Hipotenusa {hipotenusa}");
    }
}