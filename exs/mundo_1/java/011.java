/*
Desafio 011
    problema: Faça um programa que leia a largura e a algura de uma parede em
    metros, calcule a sua área e a quantidade de tinta necessária para
    pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
resolução:
*/
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner x = new Scanner(System.in);
        System.out.print("Largura: ");
        float largura = x.nextFloat();
        System.out.print("Altura: ");
        float altura = x.nextFloat();
        float area = largura * altura;
        System.out.printf("%.2fL de tinta\n", area/2);
    }
}
