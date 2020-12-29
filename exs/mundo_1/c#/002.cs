// Crie um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada 

using System;

class Program {
    public static string input(string text) {
        Console.Write(text);
        return Console.ReadLine();
    }
    
    public static void Main() {
        int dia = int.Parse(input(
            "Qual o dia do seu nascimento? "
        ));
        int mes = int.Parse(input(
            "E o mês? [0-12] "
        ));
        int ano = int.Parse(input(
            "Por fim, qual o ano? "
        ));
        
        Console.WriteLine($"Você nasceu em {dia}/{mes}/{ano}");
    }
}
