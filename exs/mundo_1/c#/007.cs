// desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

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
      float nota1 = float.Parse(io.input("Digite a primeira nota: "));
      float nota2 = float.Parse(io.input("Digite a segunda nota: "));

      float media = ((nota1 + nota2) / 2);

      io.print($"A média das notas {nota1} e {nota2} é {media}");
    }
}