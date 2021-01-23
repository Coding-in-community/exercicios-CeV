/*
    ### 028 - Jogo da Adivinhação v1.0
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
    e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu ou perdeu
 */


import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int numeroComputador;
        int numeroUsuario;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um numero: ");
        numeroUsuario = scanner.nextInt();

        Random random = new Random();
        numeroComputador = random.nextInt(5);
        if (numeroComputador == numeroUsuario)
        {
            System.out.println("Usuario venceu");
        }
        else
        {
            System.out.println("Computador venceu");
        }
    }
}
