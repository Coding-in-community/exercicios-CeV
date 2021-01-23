/*
    ### 035 - Analisando triângulo v1.0
    Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
 */


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int a, b, c;
        boolean triangulo = false;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite A: ");
        a = scanner.nextInt();

        System.out.println("Digite B: ");
        b = scanner.nextInt();

        System.out.println("Digite C: ");
        c = scanner.nextInt();

        if (a + b > c)
        {
            if (b + c > a)
            {
                if (a + c > b)
                {
                    triangulo = true;
                }
            }
        }
        if (triangulo)
        {
            System.out.println("Pode formar um triangulo");
        }
        else
        {
            System.out.println("Não pode formar um triangulo");
        }
    }
}
