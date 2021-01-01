/*
Desafio 002
Problema: Faça um programa que leia o nome de uma pessoa e mostre
        uma mensagem de boas-vindas.
Resolução do problema:
*/
import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in); // Input
        System.out.print("Digite seu nome: ");
        String nome = scan.nextLine(); // armazena o input a variavel 'nome'
        System.out.printf("Prazer, %s%n", nome);
    }
}
