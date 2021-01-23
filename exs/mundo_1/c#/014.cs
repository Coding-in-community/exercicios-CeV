/*
Desafio 014

Problema: Conversor de temperaturas: escreva um programa que converta uma temperatura 
          digitada em ºC para ºF

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
        double temperatura_C = double.Parse(
          io.input("Informe a temperatura em °C: ")
        );

        double temperatura_F =  1.8 * temperatura_C + 32;

        io.print($"Temperatura: {temperatura_F}°F");
    }
}