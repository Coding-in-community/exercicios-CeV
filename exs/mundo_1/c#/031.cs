using System;

/*
	031 - Custo da viagem
  	Desenvolva um programa que pergunte a distância de uma viagem em Km.
	Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas
*/
					
public class Program
{
	public static void Main()
	{
		Console.Write("Digite a distancia da viagem em km: ");
		float km = float.Parse(Console.ReadLine());
		float valorTotal;
		if (km <= 200)
		{
			valorTotal = 0.5f * km;
		}
		else
		{
			valorTotal = 0.45f * km;	
		}
        Console.Write("Valor total: " + valorTotal);
	}
}
