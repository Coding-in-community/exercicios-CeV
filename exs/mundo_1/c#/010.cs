// crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

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
      double valor = int.Parse(io.input("Digite o valor em real: R$"));

      double cotacaoDolar = 5.21;
      // aparentemente divisão só funciona com double
      // essa gambiarra formata o valor com dois digitos depois da virgula  
      double dolarObtido = Math.Truncate((valor / cotacaoDolar * 100)) / 100;

      io.print($"Você pode comprar ${dolarObtido}");
    }
}