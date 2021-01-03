const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

//Entrada de dados 
let velo = input("Velocidade do carro: ")

// Verificando se a velocidade esta acima do limte com if e else
if(velo > 80){
    console.log(`Você está acima do limite permitido! Velocidade de ${velo}`)
    let multa = 7 * (velo-80)
    console.log(`Sua multa é de ${multa.toFixed(2)} `)
}
else {
    console.log("Velocidade dentro do limite. Boa viagem.")
}