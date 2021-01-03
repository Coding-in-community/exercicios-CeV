/*
Desafio 027

Problema: Faça um programa que leia o nome completo de uma
          pessoa, mostrando em seguida o primeiro e o último
          nome separadamente.

Resolução do problema:
*/

//Iniciando o programa 

let nome = "Tertuliano da Silva Moraes Menezes Bueno de Andrada"

//Colocando o nome dentro de um array
const array  = nome.split('  ')

//Pegando o primeiro nome
const getFirstName = nome.slice(0,10)

//Pegando o Ultimo nome
const getlastName = nome.slice(43)

console.log(getfirstName) //Executando o primeiro nome
console.log(getlastName) // Execuntando o segundo nome
