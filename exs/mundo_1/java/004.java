/*
Desafio 004
Problema: Faça um programa que leia algo pelo teclado e mostre na tela
        seu tipo primitivo e todas as informações possíveis sobre ela.
Resolução do problema:
*/
import java.util.Scanner;
import java.util.regex.Matcher;

class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Digite algo: ");

        String algo = scan.nextLine();
        String algo_type = algo.getClass().getSimpleName(); // get var type

        System.out.printf("Tipo primitivo desse valor: %s\n", algo_type);
        System.out.printf("É um número? %s\n", isNumeric(algo));
        System.out.printf("É alfanumérico? %s\n", algo.matches("[a-zA-Z0-9]*"));
        System.out.printf("É um texto? %s\n", algo.matches("[A-Za-z]+"));
        System.out.printf("É decimal? %s\n", isDecimal(algo));
        System.out.printf("É um indentificador? %s\n", isIdentifier(algo));
        System.out.printf("É lowercase? %s\n", isLower(algo));
        System.out.printf("É upperrcase? %s\n", isUpper(algo));
        System.out.printf("É um espaço? %s\n", isSpace(algo));
        System.out.printf("Está capitalizada? %s\n", isTitle(algo));
    }

    public static boolean isNumeric(String str) {
       if (str == null)
            return false;
        return str.matches("-?\\d+");
    }

    public static boolean isDecimal(String str) {
        if (str == null)
            return false;
        String regex = "^\\d*\\.\\d+|\\d+\\.\\d*$";
        if (str.matches(regex))
            return true;
        else
            return false;
    }

    public static boolean isIdentifier(String s) {
        // an empty or null string cannot be a valid identifier
        if (s == null || s.length() == 0) {
           return false;
        }

        char[] c = s.toCharArray();
        if (!Character.isJavaIdentifierStart(c[0])) {
            return false;
        }

        for (int i = 1; i < c.length; i++) {
            if (!Character.isJavaIdentifierPart(c[i])) {
               return false;
            }
        }

        return true;
    }

    public static boolean isLower(String str){
        if (str.matches("[a-zA-Z]+") == false)
            return false;

        // convert string to char array
        char[] charArray = str.toCharArray();
        
        for(int i=0; i < charArray.length; i++){
            
            //if the character is a letter
            if( Character.isLetter(charArray[i]) ){

                //if any character is not in lower case, return false
                if( !Character.isLowerCase( charArray[i] ))
                    return false;
            }
        }
        return true; 
    }

    public static boolean isUpper(String str){ 
        if (str.matches("[a-zA-Z]+") == false)
            return false;

        //convert String to char array
        char[] charArray = str.toCharArray();
        
        for(int i=0; i < charArray.length; i++){
            
            //if the character is a letter
            if( Character.isLetter(charArray[i]) ){
 
                //if any character is not in upper case, return false
                if( !Character.isUpperCase( charArray[i] ))
                    return false;
            }
        }
        return true; 
    }

    public static boolean isSpace(String str) {
        for (int i = 0; i < str.length(); i++) {
            // if character is not equal a whitespace
            if (str.charAt(i) != " ".charAt(0))
                return false;
        }
        return true;
    }

    public static boolean isTitle(String str) {
        for (int i = 0; i < str.length(); i++) {
            // ignores whitespaces
            if (str.charAt(i) != " ".charAt(0))
                // if character is uppercase, return true
                if (Character.isUpperCase(str.charAt(i)))
                    return true;
        }
        return false;
    }
}
