using System;

/*
	033 - Maior e menor valores
  	Faça um programa que leia três números e mostre qual é o maior e qual é o menor
*/
					
public class Program
{
	public static void Main()
	{
		int menor = 0, maior = 0, val;
		bool menorSetado = false;
		for (int i = 0; i < 3; i++)
		{
			Console.Write("Digite o valor "+ (i + 1) +": ");
			val = Int32.Parse(Console.ReadLine());
			if (!menorSetado)
			{
				menor = val;
				maior = val;
				menorSetado = !menorSetado;
			}
			if (val > maior)
			{
				maior = val;
			}
			if (val < menor)
			{
				menor = val;
			}
		}
		Console.Write("maior " + maior + " menor " + menor);
	}
}

