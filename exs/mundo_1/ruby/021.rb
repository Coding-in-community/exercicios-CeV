=begin
Desafio 021

Problema: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

Resolução do problema:
=end

musica = "musica.mp3" #coloque o caminho da sua musica aqui

system("start #{musica}")

=begin
	Se você estiver usando um sistema unix (Linux ou MAC OS), 
	também podera executar assim:

	pid = fork{ exec 'afplay', "musica.mp3" }
=end