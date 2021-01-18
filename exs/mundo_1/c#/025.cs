/*
Desafio 025

Problema: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

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
    string nome = io.input("Insira um nome: ");

    string[] splitNome = nome.Split(' ');
    bool silva = Array.Exists(splitNome, elem => elem.ToLower() == "silva");

    io.print(silva);
  }
}