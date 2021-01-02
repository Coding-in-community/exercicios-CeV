/*
 * Desafio 006
 * problema: Crie um algoritmo que leia um número e mostre o seu dobro, o seu 
 * triplo e sua raiz quadrada.
 *
 * Resolução:
*/
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.printf("Número: ");
        int num = scan.nextInt();
        System.out.printf("Dobro = %d\n", num*2);
        System.out.printf("Triplo = %d\n", num*3);
        System.out.printf("Square root = %f\n", Math.sqrt(num));
    }
}
