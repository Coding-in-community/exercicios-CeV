/*
Desafio 019

Problema: Um professor quer sortear um dos seus quatro alunos para 
          apagar o quadro. Faça um programa que ajude ele, lendo o 
          nome deles e escrevendo o do escolhido

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
        string nome1 = io.input("1º aluno(a): ");
        string nome2 = io.input("2º aluno(a): ");
        string nome3 = io.input("3º aluno(a): ");
        string nome4 = io.input("4º aluno(a): ");

        string[] alunos = {
          nome1,
          nome2,
          nome3,
          nome4
        };

        Random random = new Random();
        int indiceAleatorio = random.Next(alunos.Length);

        string escolha = alunos[indiceAleatorio];

        io.print($"O aluno escolhido foi {escolha}");
    }
}