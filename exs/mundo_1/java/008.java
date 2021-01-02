/*
 * Desafio 008
 *   Problema: Escreva um programa que leia um valor em metros e o
 *   exiba convertido em centímetros e milímetros.
 *   Resolução do problema:
*/
import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner x = new Scanner(System.in);
        System.out.print("Metros: ");
        float metros = x.nextFloat();
        System.out.println("Centímetros: " + metros*100 + "cm");
        System.out.println("Milímetros: " + metros*1000 + "mm");
    }
}
