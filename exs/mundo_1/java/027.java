/*
    ### 027 - Primeiro e último nome de uma pessoa
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String nome;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o nome completo de uma pessoa: ");
        nome = scanner.nextLine();

        String [] nomeSplitado = nome.split(" ");
        System.out.println("Primeiro nome: " + nomeSplitado[0]);
        System.out.println("Ultimo nome: " + nomeSplitado[nomeSplitado.length - 1]);

    }

}
