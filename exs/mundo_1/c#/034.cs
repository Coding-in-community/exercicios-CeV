using System;

/*
	034 - Aumentos múltiplos
  	Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de R$ 15%
*/
					
public class Program
{
	public static void Main()
	{
		float salario = float.Parse(Console.ReadLine());
		float salarioFinal;
		if (salario > 1250.0f)
		{
			salarioFinal = salario * 1.10f;
		}
		else
		{
			salarioFinal = salario * 1.15f;
		}
		Console.Write("Salario final: " + salarioFinal);
	}
}

