/*
    ### 024 - Verificando as primeiras letras de um texto
    Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String nome;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o nome de uma cidade: ");
        nome = scanner.nextLine();

        if (nome.startsWith("Santo"))
        {
            System.out.println("Começa");
        }
        else
        {
            System.out.println("Não começa");
        }
    }

}
