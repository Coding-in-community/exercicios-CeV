// crie um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada 

using System;

class Program {
    // criado para facilitar a entrada de dados, baseado no input do python
    // static serve para ser lido sem instância de classe. é importante, recomendo estudar
    public static string input(string text) {
        Console.Write(text);
        return Console.ReadLine();
    }
    
    // removido o "string[] args" por não ser necessário
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

// int.Parse transforma uma string em inteiro, outros tipos tem o mesmo método como:  float.Parse, doble.Parse
// para transformas de volta em string pode se usar variável.ToString