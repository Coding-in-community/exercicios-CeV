// Faça um programa que leia o comprimento do cateto oposto (co) e do cateto
// adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento
// da hipotenusa

import java.util.Scanner;
import java.lang.*;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Cateto oposto: ");
        double co = scan.nextDouble();
        System.out.print("Cateto adjacente: ");
        double ca = scan.nextDouble();

        System.out.printf("Hipotenusa: %f\n", Math.hypot(co, ca));
    }
}
