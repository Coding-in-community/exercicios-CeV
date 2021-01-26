/*
    ### 023 - Separando dígitos de um número
    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int numero, uni, de, ce, mi;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um numero: ");
        numero = scanner.nextInt();

        uni = numero / 1 % 10;
        de = numero / 10 % 10;
        ce = numero / 100 % 10;
        mi = numero / 1000 % 10;

        System.out.println("Unidade: " + uni + "\nDezena: " + de + "\nCentena: " + ce + "\nMilhar: " + mi);

    }

}
