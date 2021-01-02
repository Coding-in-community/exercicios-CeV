/*
Desafio 003
   Problema: Crie um programa que leia dois números e mostre a soma entre eles.
Resolução do problema:
*/
import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Digite o primeiro número: ");
        int num1 = scan.nextInt();
        System.out.print("Digite o segundo número: ");
        int num2 = scan.nextInt();
        System.out.printf("%d + %d = %d\n", num1, num2, num1+num2);
    }
}
