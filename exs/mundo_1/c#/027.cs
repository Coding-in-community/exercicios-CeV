/*
Desafio 027

Problema: Faça um programa que leia o nome completo de uma
          pessoa, mostrando em seguida o primeiro e o último
          nome separadamente.

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
    string nome = io.input("Digite seu nome completo: ");

    string[] listaNome = nome.Split(' ');

    string primeiroNome = listaNome[0];
    string ultimoNome = listaNome[listaNome.Length - 1];

    io.print($"Primeiro nome: {primeiroNome}");
    io.print($"Ultimo nome: {ultimoNome}");
  }
}