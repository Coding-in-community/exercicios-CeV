/*
Desafio 028

Problema: Escreva um programa que faça o computador "pensar"
          em um número inteiro entre 0 e 5 e peça para o usuário
          tentar descobrir qual foi o número escolhido pelo computador.
          O programa deverá escrever na tela se o usuário venceu ou perdeu.

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
    Random rng = new Random();
    int maquina = rng.Next(0, 6);

    int chute = int.Parse(io.input(
      "Adivinhe o número um número entre 0 e 5: "
    ));

    if (maquina == chute) {
      io.print("Você acertou!");
    }

    else {
      io.print($"Você errou. O número escolhido foi {maquina}");
    }
  }
}