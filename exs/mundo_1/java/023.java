/*
    ### 023 - Separando dígitos de um número
    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String numero;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um numero: ");
        numero = scanner.nextLine();

        for (char n : numero.toCharArray()) {
            System.out.print(n + " ");
        }
    }

}
