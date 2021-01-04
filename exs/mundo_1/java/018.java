// Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
// seno, cosseno e tangente desse ângulo

import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Informe um ângulo: ");

        double ang = scan.nextDouble();
        double rad = Math.toRadians(ang);
        
        System.out.println("Seno: "+Math.sin(rad));
        System.out.println("Cosseno: "+Math.cos(rad));
        System.out.println("Tangente: "+Math.tan(rad));
    }
}
