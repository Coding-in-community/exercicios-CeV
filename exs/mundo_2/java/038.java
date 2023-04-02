/*
Desafio 038

Problema: Escreva um programa que leia dois números inteiros e compare-os.
          mostrando na tela uma mensagem:
            - O primeiro valor é maior
            - O segundo valor é maior
            - Não existe valor maior, os dois são iguais

Resolução do problema:
*/

import java.util.Scanner;

class Main{
    public static void main(String[] args) {

        // instancia a classe Scanner
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um numero abaixo: ");
        double numero1 = scanner.nextInt();

        System.out.println("Digite outro número:");
        double numero2 = scanner.nextInt();

        if (numero1 > numero2) {
            System.out.println("O primeiro número é maior");
        } else if (numero1 < numero2) {
            System.out.println("O segundo número é maior");
        } else System.out.println("Não existe maior, os dois são IGUAIS!");

    }
}