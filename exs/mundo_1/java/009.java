/*
Desafio 009
Problema: Faça um programa que leia um número Inteiro qualquer e mostre na
    tela a sua tabuada.
Resolução do problema:
*/
import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Número: ");
        int num = scan.nextInt();
        System.out.printf("%d x 0 = %d\n", num, num*0);
        System.out.printf("%d x 1 = %d\n", num, num*1);
        System.out.printf("%d x 2 = %d\n", num, num*2);
        System.out.printf("%d x 3 = %d\n", num, num*3);
        System.out.printf("%d x 4 = %d\n", num, num*4);
        System.out.printf("%d x 5 = %d\n", num, num*5);
        System.out.printf("%d x 6 = %d\n", num, num*6);
        System.out.printf("%d x 7 = %d\n", num, num*7);
        System.out.printf("%d x 8 = %d\n", num, num*8);
        System.out.printf("%d x 9 = %d\n", num, num*9);
        System.out.printf("%d x 10 = %d\n", num, num*10);
    }
}
