using System;

/*
	032 - Ano bissexto
  	Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
*/
					
public class Program
{
	public static void Main()
	{
		Console.Write("Digite o ano: ");
		int ano = Int32.Parse(Console.ReadLine());
		if (ano % 100 != 0 && ano % 4 == 0 || ano % 400 == 0)
		{
			Console.Write("É bissexto\n");	
		}
		else
		{
			Console.Write("Não é bissexto\n");		
		}
	}
}

