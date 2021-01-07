=begin
Desafio 046

Problema: Faça um programa que mostre na tela uma contagem regressiva
          para o estouro de fogos de artifício, indo de 10 até 0, com
          pausa de 1 segundo entre eles.

Resolução do problema:
=end
#a = "\x0c[%%-%vs]",col
for i in 0..10
	system('cls')
	puts "[" + "="*i + ">" + " "*(10-i) +"]" + " %#{i*10}"
	sleep(1)
end

puts"A QUEIMA DE FOGOS VAI COMEÇAR!!"

#Uma solução sem fazer uma barrinha de progresso:

=begin
contador = 10

for i in 1..10
	puts contador - i
	sleep(1)
end

puts"A QUEIMA DE FOGOS VAI COMEÇAR!!"

=end

