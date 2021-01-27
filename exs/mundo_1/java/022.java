/*
    ### 022 - Analisador de textos
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    em letras maiúsculas, minúsculas, a quantidade de letras sem espaço e quantas letras tem o primeiro nome
 */


import java.util.Locale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String nome;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite seu nome: ");
        nome = scanner.nextLine();

        System.out.println("Maiusculas: " + nome.toUpperCase(Locale.ROOT));
        System.out.println("Minusculas: " + nome.toLowerCase(Locale.ROOT));
        System.out.println("Quantidade de letras sem espaço: " + nome.replaceAll(" ", "").length());
        System.out.println("Quantidade de lestras do primeiro nome: " + nome.split(" ")[0].length());

    }

}
