// escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

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
      float metros = float.Parse(io.input("Digite o valor em metros: "));

      float decimetros = (metros * 10);
      float centimetros = (metros * 100);
      float milimetros = (metros * 1000);

      io.print($"Metros: {metros}");
      io.print($"Decímetros: {decimetros}");
      io.print($"Centímetros: {centimetros}");
      io.print($"Milímetros: {milimetros}");
    }
}