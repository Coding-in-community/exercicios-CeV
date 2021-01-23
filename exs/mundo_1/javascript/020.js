/*
Desafio 020

Problema: O mesmo professor do desafio anterior quer sortear a ordem de 
          apresentação de trabalhos dos alunos. Faça um programa que leia o 
          nome dos quatro alunos e mostre a ordem sorteada

Resolução do problema:
*/

const input = require('readline-sync').question

let nome1 = input('1º aluno(a): ')
let nome2 = input('2º aluno(a): ')
let nome3 = input('3º aluno(a): ')
let nome4 = input('4º aluno(a): ')

let alunos = [
    nome1,
    nome2,
    nome3,
    nome4
]

let quantidadeAlunos = alunos.length // ou 4

// indice assume 0, 1, 2 ou 3 em ordem crescente
for (let indice = 0; indice < quantidadeAlunos; indice++) {
    // indiceAleatorio pode assumir 0, 1, 2 ou 3 sem ordem especifica 
    let indiceAleatorio = Math.trunc(Math.random() * quantidadeAlunos)

    // copia o nome de um aluno 
    let alunoAleatorio = alunos[indiceAleatorio]

    // remove esse aluno da sua posição na lista
    alunos.splice(indiceAleatorio, 1)

    // adiciona ele no final
    alunos.push(alunoAleatorio) 
}

console.log(`Ordem: ${alunos.join(', ')}`)