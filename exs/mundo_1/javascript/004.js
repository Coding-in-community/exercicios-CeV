/*
Desafio 004

Problema: Faça um programa que leia algo pelo teclado e mostre na tela
          seu tipo primitivo e todas as informações possíveis sobre ela.

Resolução do problema:
*/

/*
AVISO:

Para a resolução dessa atividade foram usados métodos complexos, ela serve de referências futuras. Não se assuste caso não entenda.
Conhecimentos recomendados: Laços de repetição, estrutura condicional, arrays e seus métodos.
*/

const input = require('readline-sync').question
const print = console.log


class checkString {
  constructor(text) {
    this.body = {}
    this.body.text = text
    this.body.array = this.body.text.split('')
  }

  type() {
    return typeof(this.body.text)
  }

  isSpace() {
    return this.body.array.every(chr => /\s/.test(chr))
  }

  isNumeric() {
    return (!isNaN(Number(this.body.text)) && !this.isSpace())
  }

  isAlpha() {
    return (this.body.array.every(chr => isNaN(Number(chr)))  && !this.isSpace())
  }

  isAlnum() {
    return (
      this.body.array.some(chr => isNaN(Number(chr))) &&
      this.body.array.some(chr => !isNaN(Number(chr))) &&
      !this.isSpace()
    ) 
  }

  isUpper(_default = this.body.text) {
    return ((_default == _default.toUpperCase()) && this.isAlpha() && !this.isSpace())
  }

  isLower(_default = this.body.text) {
    return ((_default == _default.toLowerCase()) && this.isAlpha() && !this.isSpace())
  }

  isCapitalize(_default = this.body.text) {
    return (
      this.isUpper(_default[0]) && 
      this.isLower(_default.slice(1))
    )
  }

  isTitle() {
    let wordList = this.body.text.split(' ')

    return wordList.every(word => this.isCapitalize(word))
  }
}

function yesOrNo(bool) {
  return bool? 'sim' : 'não'
}

let text = input("Digite algo: ")
checker = new checkString(text)

print('O tipo é ' + checker.type())
print('São apenas espaços? ' + yesOrNo(checker.isSpace()))
print('São apenas números? ' + yesOrNo(checker.isNumeric()))
print('São apenas letras? ' + yesOrNo(checker.isAlpha()))
print('São apenas letras e números? ' + yesOrNo(checker.isAlnum()))
print('São apenas maiúsculas? ' + yesOrNo(checker.isUpper()))
print('São apenas minúsculas? ' + yesOrNo(checker.isLower()))
print('É capitalizado? ' + yesOrNo(checker.isCapitalize()))
print('É um título? ' + yesOrNo(checker.isTitle()))