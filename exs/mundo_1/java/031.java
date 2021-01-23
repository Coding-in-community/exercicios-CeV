/*
    ### 031 - Custo da viagem
    Desenvolva um programa que pergunte a distância de uma viagem em Km.
    Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        float km, valorTotal;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite a distancia da viagem em km: ");
        km = scanner.nextFloat();

        if (km <= 200) {
            valorTotal = 0.5f * km;
        }
        else {
            valorTotal = 0.45f * km;
        }
        System.out.println("Valor total: " + valorTotal);
    }
}
