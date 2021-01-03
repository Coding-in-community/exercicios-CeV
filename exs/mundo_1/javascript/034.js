const input = require('readline-sync').question //Chamando o modulo readline-sync para entrada de dados

let sal = input("Digite seu salário: ") // Entrada de dados

//Condição para o controle dos salários de 10% e 15%
if (sal > 1250) {
 let aumento = sal*10/100
 let calculo = Number(aumento) + Number(sal) //O Number é para determinar que a variável é do tipo numero e não string.
 console.log(`Com o aumento de 10%, o seu salário foi de R$ ${sal} para ${calculo}.`)
}
else {
    let aumento = sal * 10/100
    let calculo = Number(aumento) + Number(sal)
    console.log(`Com o aumento de 15%, o seu salário foi de R$ ${sal} para ${calculo}`)
}

