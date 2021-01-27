/*
    ### 026 - Primeira e última ocorrência de uma string
    Faça um programa que leia uma frase qualquer e mostre: quantas vezes aparece a letra "a",
    em que posição ela aparece a primeira vez em que posição ela aparece a última vez
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String frase;
        int contador = 0;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite uma frase qualquer: ");
        frase = scanner.nextLine();

        for (int i = 0; i < frase.length(); i++)
        {
            if (frase.toCharArray()[i] == 'a') contador++;
        }
        System.out.println("a apareceu: " + contador + " vezes");
        System.out.println("Posicao da primeira vez: " + frase.indexOf("a"));
        System.out.println("Posicao da ultima vez: " + frase.lastIndexOf("a"));
    }

}
