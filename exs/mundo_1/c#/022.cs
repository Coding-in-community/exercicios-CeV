/*
Desafio 022

Problema: Crie um programa que leia o nome completo de uma pessoa
          e mostre:
              - O nome com todas as letras maiúsculas e minúsculas.
              - Quantas letras ao todo(sem considerar espaços)
              - Quantas letras tem o primeiro nome.

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

    string nomeMaiusculo = nome.ToUpper();
    string nomeMinusculo = nome.ToLower();
    int qntdLetrasNomeCompleto = nome
      .Replace(" ", "")
      .Length;
    int qntdLetrasPrimeiroNome = nome
      .Split(' ')[0]
      .Length;


    io.print($"Nome maíusculo: {nomeMaiusculo}");
    io.print($"Nome minúsculo: {nomeMinusculo}");
    io.print($"Quantidade de letras que o nome completo tem: {qntdLetrasNomeCompleto}");
    io.print($"Quantidade de letras que apenas o primeiro nome tem: {qntdLetrasPrimeiroNome}");
  }
}