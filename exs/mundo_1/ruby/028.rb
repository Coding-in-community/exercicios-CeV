=begin
Desafio 028

Problema: Escreva um programa que faça o computador "pensar"
          em um número inteiro entre 0 e 5 e peça para o usuário
          tentar descobrir qual foi o número escolhido pelo computador.
          O programa deverá escrever na tela se o usuário venceu ou perdeu.

Resolução do problema:
=end

pc = rand(1..5)

print'Adivinhe o número um número entre 0 e 5: '
chute = gets.chomp.to_i

if chute == pc
    puts'Você ACERTOU!'
else
    puts'Você ERROU!'
    puts"O número era #{pc}"
end