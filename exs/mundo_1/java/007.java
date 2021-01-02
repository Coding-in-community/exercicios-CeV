import java.util.*;

class Main {
    public static void main(String[] args){
        Scanner x = new Scanner(System.in);
        System.out.print("Primeira nota: ");
        int nota1 = x.nextInt();
        System.out.print("Segunda nota: ");
        int nota2 = x.nextInt();
        float media = (nota1 + nota2) / 2;
        System.out.printf("Média = %.1f\n", media);
    }
}
