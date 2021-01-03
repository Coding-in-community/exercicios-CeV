const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados
let a = input("Primeiro segmento de reta: \n")
let b = input("Segundo segmento de reta: \n")
let c = input("Terceiro segmento de reta: \n")

//Condição if e else para saber se as partes formam um triângulo
if (a < b + c && b < a + c && c + a  > b){
    console.log("O triângulo existe.")
}

else {
    console.log("O triângulo não pode existir.")
}

//O operador || significa "OU" e o operador && significa "E"