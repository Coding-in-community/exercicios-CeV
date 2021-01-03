// crie um script que leia dois números e tente mostrar a soma entre eles

using System;

// input separado em uma classe própria, para facilitar a leitura
class IO {
    // criado para facilitar a entrada de dados, baseado no input do python
    public string input(string text) {
        Console.Write(text);
        return Console.ReadLine();
    }
}

class Program {
    // static serve para ser lido sem instância de classe. é importante, recomendo estudar
    public static void Main() {
        // instância da classe
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

// float.Parse transforma uma string em flutuante, outros tipos tem o mesmo método como:  int.Parse, doble.Parse
// para transformas de volta em string pode se usar variável.ToString