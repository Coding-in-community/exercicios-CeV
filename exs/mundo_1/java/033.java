/*
    ### 033 - Maior e menor valores
    Faça um programa que leia três números e mostre qual é o maior e qual é o menor
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int maior = 0, menor = 0, valor;
        boolean valoresSetados = false;
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            System.out.println("Digite o valor " + (i + 1) + ": ");
            valor = scanner.nextInt();
            if(!valoresSetados)
            {
                menor = valor;
                maior = valor;
                valoresSetados = !valoresSetados;
            }
            if (valor > maior)
            {
                maior = valor;
            }
            if (valor < menor)
            {
                menor = valor;
            }
        }
        System.out.println("Maior: " + maior + " Menor: " + menor);
    }
}
