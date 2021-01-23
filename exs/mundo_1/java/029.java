/*
    ### 029 - Radar eletrônico
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada Km acima do limite.
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int kmh;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite a velocidade do carro em km: ");
        kmh = scanner.nextInt();

        if (kmh > 80)
        {
            System.out.println("Este veiculo foi multado");
            System.out.println("Multa: " + (kmh - 80) * 7 + " reais");
        }

    }
}
