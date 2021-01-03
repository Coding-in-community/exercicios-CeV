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
    return this.body.array.every(chr => !isNaN(Number(chr)))
  }

  isAlpha() {
    return this.body.array.every(chr => isNaN(Number(chr)))
  }

  isAlnum() {
    return (
      this.body.array.some(chr => isNaN(Number(chr))) &&
      this.body.array.some(chr => !isNaN(Number(chr)))
    ) 
  }

  isUpper(_default = this.body.text) {
    return (_default == _default.toUpperCase())
  }

  isLower(_default = this.body.text) {
    return (_default == _default.toLowerCase())
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


let text = input("Digite algo: ")
checker = new checkString(text)

print(checker.type())
print(checker.isSpace())
print(checker.isNumeric())
print(checker.isAlpha())
print(checker.isAlnum())
print(checker.isUpper())
print(checker.isLower())
print(checker.isCapitalize())
print(checker.isTitle())

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
    return this.body.array.every(chr => !isNaN(Number(chr)))
  }

  isAlpha() {
    return this.body.array.every(chr => isNaN(Number(chr)))
  }

  isAlnum() {
    return (
      this.body.array.some(chr => isNaN(Number(chr))) &&
      this.body.array.some(chr => !isNaN(Number(chr)))
    ) 
  }

  isUpper(_default = this.body.text) {
    return (_default == _default.toUpperCase())
  }

  isLower(_default = this.body.text) {
    return (_default == _default.toLowerCase())
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


let text = input("Digite algo: ")
checker = new checkString(text)

print(checker.type())
print(checker.isSpace())
print(checker.isNumeric())
print(checker.isAlpha())
print(checker.isAlnum())
print(checker.isUpper())
print(checker.isLower())
print(checker.isCapitalize())
print(checker.isTitle())