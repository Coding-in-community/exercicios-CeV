/*
    ### 032 - Ano bissexto
    Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int ano;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o ano: ");
        ano = scanner.nextInt();

        if (ano % 100 != 0 && ano % 4 == 0 || ano % 400 == 0) {
            System.out.println("É bissexto");
        }
        else
        {
            System.out.println("Não é bissexto");
        }

    }
}
