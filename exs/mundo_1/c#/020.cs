/*
Desafio 020

Problema: O mesmo professor do desafio anterior quer sortear a ordem de 
          apresentação de trabalhos dos alunos. Faça um programa que leia o 
          nome dos quatro alunos e mostre a ordem sorteada

Resolução do problema:
*/

using System;
using System.Collections.Generic;

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

class random {
  public static List<string> shuffle(String[] array){
    Random random = new Random();        
    var list = new List<string>(array);
    
    int size = list.Count;
    
    for (int i = size; i > 0; i--){
      int randindex = random.Next(size-1);
      var aux = list[randindex];
      list.Add(aux);
      list.RemoveAt(randindex);
    }

    return list;
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

        List<string> alunosAleatorio = random.shuffle(alunos);

        io.print(string.Join(
          System.Environment.NewLine,
          alunosAleatorio
        ));
    }
}