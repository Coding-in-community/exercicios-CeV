/*
Desafio 029

Problema: Escreva um programa que leia a velocidade de um carro.
          Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
          que ele foi multado. A multa vai custar R$7,00 por cada
          Km acima do limite.

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
    float velocidade = float.Parse(io.input(
      "Informe a velocidade do carro: "
    ));

    if (velocidade > 80) {
      float multa = (velocidade - 80) * 7;
      float fixedMulta = (float) Math.Truncate(multa * 100) / 100;

      io.print($"Você foi multado em R${fixedMulta}");
    }
  }
}