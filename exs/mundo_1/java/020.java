// O mesmo professor do desafio anterior quer sortear a ordem de apresentação
// de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
// e mostre a ordem sorteada

import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> alunos = new ArrayList<>();

        System.out.print("Nome do aluno: ");
        alunos.add(scan.nextLine());

        System.out.print("Nome do aluno: ");
        alunos.add(scan.nextLine());

        System.out.print("Nome do aluno: ");
        alunos.add(scan.nextLine());

        System.out.print("Nome do aluno: ");
        alunos.add(scan.nextLine());

        Collections.shuffle(alunos);
        System.out.println("Ordem de apresentação: " + alunos);
    }
}
