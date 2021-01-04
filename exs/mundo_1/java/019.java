// Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
// Faça um programa que ajude ele, lendo o nome deles e escrevendo o escolhido

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

        int index = new Random().nextInt(alunos.size()); // select a index
        System.out.printf("\n%s vai apagar o quadro\n", alunos.get(index));
    }
}
