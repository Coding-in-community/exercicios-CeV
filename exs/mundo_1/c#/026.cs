/*
Desafio 026

Problema: Faça um programa que leia uma frase pelo teclado
          e mostre quantas vezes aparece a letra "A", em que
          posição ela aparece a primeira vez e em que posição
          ela aparece a última vez.

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
    string frase = io.input("Digite uma frase qualquer: ");
    string lowerFrase = frase.ToLower();

    int primeiraOcorrencia = lowerFrase.IndexOf('a');
    int ultimaOcorrencia = lowerFrase.LastIndexOf('a');

    int lengthFrase = lowerFrase.Length;
    int lengthFraseSemA = lowerFrase.Replace("a", "").Length;
    int lengthA = (lengthFrase - lengthFraseSemA);

    io.print($"Quantas vezes a letra \"A\" apareceu: {lengthA}");
    io.print($"Ela aparece a primeira vez na posição: {primeiraOcorrencia + 1}");  
    io.print($"Ela aparece a ultima vez na posição: {ultimaOcorrencia + 1}");
  }
}