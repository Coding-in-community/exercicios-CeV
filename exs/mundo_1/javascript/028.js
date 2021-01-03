/*
Desafio 028

Problema: Escreva um programa que faça o computador "pensar"
          em um número inteiro entre 0 e 5 e peça para o usuário
          tentar descobrir qual foi o número escolhido pelo computador.
          O programa deverá escrever na tela se o usuário venceu ou perdeu.

Resolução do problema:
*/

const input = require('readline-sync').question //Importando input do NPM

//Mensagem de boas vindas
console.log("Vou pensar em um numero de 0 a 5")

//Entrada de dados
let num = input("Em qual numero vc acha que eu pensei?: ")

let computador =  Math.floor(Math.random()*5); // Sorteando numeros entre 0 a 5

//Mensagem de erro caso o usuário digitar um numero maior que 5
if(num > 5){
   console.log("Voce só pode digitar numero de 0 a 5, tente novamente")
}

// Condição para saber quem ganhou se foi o computador ou o usuário
else {
    if(num == computador){
        console.log("Voce ganhou, parabéns!")
    }
    else { 
        console.log("Eu ganhei!!")
    }
}





