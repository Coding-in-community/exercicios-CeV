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





