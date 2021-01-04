// Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
// salário, com 15% de aumento

import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner x = new Scanner(System.in);
        System.out.print("Salário: ");
        float salario = x.nextFloat();
        String aumento = String.format("%.2f", salario+((salario * 15) / 100));
        System.out.println("Salário com 15% de aumento: R$" + aumento);
    }
 }
