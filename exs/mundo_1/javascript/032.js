const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

let ano = input("Descubra se um ano é bissexto: ")

if(  ano % 4 == 0 && ano % 100 != 0 || ano % 400 == 0 ){
    console.log("O ano é bissexto")
}
else {
    console.log("O ano não é bissexto")
}