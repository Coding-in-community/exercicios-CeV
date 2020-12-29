// Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

using System;

static class IO {
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
        int num = (int) float.Parse(
          IO.input("Digite um número: ")
        );

        IO.print(
          $"O antecessor é {num - 1}"
        );
        IO.print(
          $"O sucessor é {num + 1}"
        );

    }
}
