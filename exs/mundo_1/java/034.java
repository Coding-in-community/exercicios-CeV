/*
    ### 034 - Aumentos múltiplos
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de R$ 15%
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        float salario, salarioFinal;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o salario: ");
        salario = scanner.nextFloat();

        if (salario > 1250.0f)
        {
            salarioFinal = salario * 1.10f;
        }
        else
        {
            salarioFinal = salario * 1.15f;
        }
        System.out.println("Salario final: " + salarioFinal);
    }
}
