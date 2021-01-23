using System;

/*
	035 - Analisando triângulo v1.0
    Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
*/		
public class Program
{
	public static void Main()
	{
		int a, b, c;
		bool triangulo = false;
		Console.WriteLine("Digite A: ");
		a = Int32.Parse(Console.ReadLine());
		Console.WriteLine("Digite B: ");
		b = Int32.Parse(Console.ReadLine());
		Console.WriteLine("Digite C: ");
		c = Int32.Parse(Console.ReadLine());
		
		if (a + b > c)
		{
			if (b + c > a)
			{
				if (a + c > b)
				{
					triangulo = true;
				}
			}
		}
		if (triangulo)
		{
			Console.WriteLine("Pode formar um triangulo");
		}
		else
		{
			Console.WriteLine("Não pode formar um triangulo");
		}
	}
}