// Crie um script que leia dois números e tente mostrar a soma entre eles

using System;

class IO {
    public static string input(string text) {
        Console.Write(text);
        return Console.ReadLine();
    }
}

class Program {
    public static void Main() {
        IO IO = new IO();
        
        float num1 = float.Parse(IO.input(
            "Qual o primeiro número? "
        ));
        float num2 = float.Parse(IO.input(
            "Digite o segundo: "
        ));
        float soma = num1 + num2;
        
        Console.WriteLine($"A soma de {num1} e {num2} é igual a {soma}");
    }
}
