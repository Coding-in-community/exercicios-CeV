/*
Desafio 037

Problema: Escreva um programa em Python que leia um número
          inteiro qualquer e peça para o usuário escolher qual
          será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

Resolução do problema:
*/

import java.util.Scanner;

class Main{
    public static void main(String[] args) {

        // instancia a classe Scanner
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int numero = scanner.nextInt();

        System.out.printf("Você digitou %d", numero);
        System.out.println("\n\nEscolha uma opção abaixo: \n[ 1 ] CONVERSÃO PARA BINÁRIO\n[ 2 ] CONVERSÃO PARA OCTAL\n[ 3 ] CONVERSÃO PARA HEXADECIMAL");
        int op = scanner.nextInt();

        if (op == 1) {
            System.out.printf("O valor %d convertido para BINÁRIO É: %s.%n", numero, Integer.toBinaryString(numero));
        } else if (op == 2) {
            System.out.printf("O valor %d convertido para OCTAL É: %s.%n", numero, Integer.toOctalString(numero));
        } else if (op == 3) {
            System.out.printf("O valor %d convertido para HEXADECIMAL É: %s.%n", numero, Integer.toHexString(numero).toUpperCase());
        } else {
            System.out.println("Opção INVÁLIDA.");
        }

        scanner.close();

    }
}