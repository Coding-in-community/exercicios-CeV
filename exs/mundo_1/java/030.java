/*
    ### 030 - Par ou ímpar?
    Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int numero;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um numero: ");
        numero = scanner.nextInt();

        if (numero % 2 == 0)
        {
            System.out.println("É par");
        }
        else
        {
            System.out.println("É impar");
        }
    }
}
