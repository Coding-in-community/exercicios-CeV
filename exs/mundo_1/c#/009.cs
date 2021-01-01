// faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

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
      int valor = int.Parse(io.input("Digite um número inteiro qualquer: "));

      io.print($"{valor} x 01 = {valor*1}");
      io.print($"{valor} x 02 = {valor*2}");
      io.print($"{valor} x 03 = {valor*3}");
      io.print($"{valor} x 04 = {valor*4}");
      io.print($"{valor} x 05 = {valor*5}");
      io.print($"{valor} x 06 = {valor*6}");
      io.print($"{valor} x 07 = {valor*7}");
      io.print($"{valor} x 08 = {valor*8}");
      io.print($"{valor} x 09 = {valor*9}");
      io.print($"{valor} x 10 = {valor*10}");
    }
}