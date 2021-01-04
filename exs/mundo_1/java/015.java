 // Escreva um programa que pergunte a quantidade de Km percorridos por um
 // carro alugado e a quantidade de dias pelos quais ele foi alugado

// Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15
// por km rodado

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Quantidade de km rodados: ");
        float rodado = scan.nextFloat();

        System.out.print("Dias com o carro: ");
        int dias = scan.nextInt();
        String price = String.format("%.2f", (dias * 60) + (rodado * 0.15));
        System.out.println("Preço total: R$"+price);
    }
}
