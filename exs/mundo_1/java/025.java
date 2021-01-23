/*
    ### 025 - Procurando uma string dentro de outra
    Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String nome;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o nome de uma pessoa: ");
        nome = scanner.nextLine();

        if (nome.contains("Silva"))
        {
            System.out.println("Contem Silva");
        }
        else
        {
            System.out.println("Não contem Silva");
        }
    }

}
