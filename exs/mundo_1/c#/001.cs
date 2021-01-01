// crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

using System;

class Program {
    // método chamado para executar o programa
    static void Main(string[] args) {
        string nome;
    
        Console.Write("Qual o seu nome? ");
        nome = Console.ReadLine();
        
        Console.WriteLine($"Bem vindo, {nome}");
    }
}

// A interpolação, método que te permite colocar uma variável no meio da string é feita usando chaves {}, também é necessário o cifrão $ no começo