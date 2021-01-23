/*
Desafio 013

Problema: Faça um algoritmo que leia o salário de um funcionário 
          e mostre seu novo salário, com 15% de aumento

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
        double salario = double.Parse(
          io.input("Informe seu sálario: R$")
        );

        double salarioFinal = Math.Truncate((salario * 1.15 * 100)) / 100;

        io.print($"O salario final é {salarioFinal}");
    }
}