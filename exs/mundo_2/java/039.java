/*
Desafio 038

Problema: Faça um programa que leia o ano de nascimento de um jovem e informe,
          de acordo com a sua idade, se ele ainda vai se alistar ao serviço
          militar, se é a hora exata de se alistar ou se já passou do tempo
          do alistamento. Seu programa também deverá mostrar o tempo que falta
          ou que passou do prazo.

Resolução do problema:
*/

import java.time.LocalDate;
import java.util.Date;
import java.util.Scanner;

class Main{
    public static void main(String[] args) {

        // instancia a classe Scanner
        Scanner scanner = new Scanner(System.in);

//        obtendo data da classe Date
//        Date d = new Date();
//        int anoAtual = d.getYear() + 1900;

        // obtendo data atual com LocalDate
        LocalDate hoje = LocalDate.now();
        int anoAtual = hoje.getYear();

        System.out.println("Digite o ano do seu nascimento abaixo: ");
        int anoNascimento = scanner.nextInt();

        int idade = anoAtual - anoNascimento;

        if (idade < 18 ) {
            System.out.printf("Você vai se alistar em %d ano(s), em %d", 18-idade, anoAtual + (18-idade));
        } else if (idade == 18) {
            System.out.println("Está na hora de se ALISTAR");
        } else System.out.printf("Passou da hora de se ALISTAR.\nVocê deveria ter se ALISTADO há %d ano(s), em %d.", idade-18, anoAtual - (idade-18));



    }
}