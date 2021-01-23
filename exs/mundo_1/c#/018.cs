/*
Desafio 018

Problema: Faça um programa que leia um ângulo qualquer e mostre 
          na tela o valor do seno, cosseno e tangente desse ângulo

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
        double graus = double.Parse(
          io.input("Informe o angulo em graus: ")
        );

        double pi = 3.14159;
        double radianos = graus * (pi / 180);

        double sen = Math.Sin(radianos);
        double cos = Math.Cos(radianos);
        double tan = Math.Tan(radianos);

        double senTrunc = Math.Truncate(sen * 100) / 100;
        double cosTrunc = Math.Truncate(cos * 100) / 100;
        double tanTrunc = Math.Truncate(tan * 100) / 100;

        io.print($"Seno {senTrunc}");
        io.print($"Cosseno {cosTrunc}");
        io.print($"Tangente {tanTrunc}");
    }
}