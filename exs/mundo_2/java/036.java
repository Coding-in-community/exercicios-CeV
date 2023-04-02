/*
Desafio 036

    Problema: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

    Resolução do problema:
*/

import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        // instancia um objeto da classe Scanner e define o input através do teclado
        Scanner scanner = new Scanner(System.in);

        // obtem os dados do usuário
        System.out.print("Informe o valor da casa: R$ ");
        double valorCasa = scanner.nextDouble();

        System.out.print("Informe o salário do comprador: R$ ");
        double salarioComprador = scanner.nextDouble();

        System.out.print("Anos de financiamento: ");
        int quantidadeAnos = scanner.nextInt();

        // obtem o valor da prestação
        double prestacao = valorCasa/(quantidadeAnos * 12);

        System.out.printf("Para pagar uma casa de %f em %d anos a prestação será de R$ %.2f", valorCasa, quantidadeAnos, prestacao);

        // prestação não pode ultrapassar 30% do valor do empregado
        if (prestacao < salarioComprador * 0.3) {
            System.out.printf("FINANCIAMENTO ACEITO!!!\nA prestação será de R$%.2f/Mês durante %d Anos.", prestacao, quantidadeAnos);
        } else {
            System.out.println("FINANCIAMENTO NEGADO!!!\nSALÁRIO INSUFICIENTE.");
        }
    }
}
