=begin
Desafio 069

Problema: Crie um programa que leia a idade e o sexo de várias
          pessoas. A cada pessoa cadastrada, o programa deverá
          perguntar se o usuário quer ou não continuar.
          No final, mostre:
            A) Quantas pessoas tem mais de 18 anos;
            B) Quantos homens foram cadastrados;
            C) Quantas mulheres tem menos de 20 anos.

Resolução do problema:
=end

qtdPessoas = 0
qtdHomem = 0
qtdMulher = 0
run = true

while run
	print"IDADE: "
	idade = gets.chomp.to_i
	print"SEXO: "
	sexo = gets.chomp.upcase

	while sexo != 'M' and sexo != 'F'
		print"Sexo incorreto, informe novamente: "
		sexo = gets.chomp.upcase
	end
 	
	if idade > 18
		qtdPessoas += 1
	end

	if sexo == 'M'
		qtdHomem += 1
	end

	if sexo == 'F' and idade < 20
		qtdMulher += 1
	end

	print"Deseja cadastrar mais uma pessoa? "
	opc = gets.chomp.upcase

	while opc != 'S' and opc != 'N'
		print"Opção inválida."
		opc = gets.chomp.upcase
	end

	if opc == 'N'
		run = false
	end
 end 

 puts "Foram cadastrados #{qtdPessoas} pessoa(s) maior(es) que 18 anos."
 puts "Foram cadastrados #{qtdHomem} homem(ns)."
 puts "Foram cadastradas #{qtdMulher} mulher(es) menor(es) que 20 anos."
