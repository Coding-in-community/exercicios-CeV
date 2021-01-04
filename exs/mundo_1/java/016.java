// Crie um programa que leia um número real qualquer pelo teclado e mostre
// na tela a sua porção inteira

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Digite um número real: ");
        double num = scan.nextDouble();
        System.out.println((int) Math.round(num)); // Convert double to int
    }
}
