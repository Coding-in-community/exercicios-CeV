// Conversor de temperaturas: escreva um programa que converta uma temperatura
// digitada em ºC para ºF
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Celsius: ");
        float celsius = scan.nextFloat();
        String fahrenheit = String.format("%.2f", (celsius * 9/5) + 32);
        System.out.println(fahrenheit+"°F");
    }
}
