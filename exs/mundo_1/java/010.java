/*
Desafio 010
Problema: Crie um programa que leia quanto dinheiro uma pessoa tem
    na carteira e mostre quantos dólares ela pode comprar.
Resolução do problema:
*/
import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Informe seu dinheiro: R$");
        float money = scan.nextFloat();
        double dolar = 5.19;
        System.out.printf("R$%.2f = $%.2f\n", money, money/dolar);
    }
}
