// Crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

using System;

class Program {
    static void Main(string[] args) {
        string nome;
    
        Console.Write("Qual o seu nome? ");
        nome = Console.ReadLine();
        
        Console.WriteLine($"Bem vindo, {nome}");
    }
}
