// faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

/*
AVISO:

Para a resolução dessa atividade foram usados métodos complexos, ela serve de referências futuras. Não se assuste caso não entenda.
Conhecimentos recomendados: Laços de repetição, estrutura condicional, arrays e seus métodos.
*/

using System;

static class io {
    // entrada de dados
    public static string input(string text) {
        Console.Write(text);
        return Console.ReadLine();
    }

    // saida de dados
    public static void print(object data, string end="\n") {
        string text = data.ToString();

        Console.Write($"{text}{end}");
    }
}

class CheckString {
  private string text;

  // método construtor
  public CheckString(string text) {
    this.text = text;
  }

  // checa o tipo
  public Type type() {
    return this.text.GetType();
  }

  // checa se há apenas números inteiros
  public bool isNumeric() {
    int digitCounter = 0;
    foreach (char letter in this.text) {
      if (char.IsDigit(letter)) {
        digitCounter += 1;
      }
    }

    return (digitCounter == this.text.Length);
  }

  // checa se há apenas letras do alfabeto
  public bool isAlpha() {
    int letterCounter = 0;
    foreach (char letter in this.text) {
      if (char.IsLetter(letter)) {
        letterCounter += 1;
      }
    }

    return (letterCounter == this.text.Length);
  }

  // checa se há letras ou números
  public bool isAlnum() {
    int letterOrDigitCounter = 0;
    foreach (char letter in this.text) {
      if (char.IsLetterOrDigit(letter)) {
        letterOrDigitCounter += 1;
      }
    }

    return (letterOrDigitCounter == this.text.Length);
  }

  // checa se há apenas espaços
  public bool isSpace() {
    int spaceCounter = 0;
    foreach (char letter in this.text) {
      if (char.IsWhiteSpace(letter)) {
        spaceCounter += 1;
      }
    }

    return (spaceCounter == this.text.Length);
  }
}

class Program {
  public static void Main () {
    string text = io.input("Digite algo: ");

    CheckString checkedText = new CheckString(text);

    io.print(text.Length);
    io.print("O tipo é " + checkedText.type());
    io.print("É um número inteiro? " + checkedText.isNumeric());
    io.print("São apenas letras? " + checkedText.isAlpha());
    io.print("São apenas letras ou números? " + checkedText.isAlnum());
    io.print("São apenas espaços? " + checkedText.isSpace());
    // maiusculo
    // minusculo
    // capitalizado
    // titulo
  }
}