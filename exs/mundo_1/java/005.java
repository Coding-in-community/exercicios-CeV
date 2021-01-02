/*
Desafio 005
Problema: Faça um programa que leia um número inteiro e mostre na tela
        o seu sucessor e antecessor.
Resolução do problema:
*/
import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Antecessor e sucessor\nDigite um número: ");
        int num = scan.nextInt();
        System.out.printf("%d - %d - %d\n", num-1, num, num+1);
    }
}
