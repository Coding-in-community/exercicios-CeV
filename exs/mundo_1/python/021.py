"""
Desafio 021

Problema: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

Resolução do problema:
"""
import pygame
from time import sleep

audio = '../assets/audio/021.mp3'

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(audio)
pygame.mixer.music.play()

# Observação:
# Em uma versão antiga o método "pygame.event.wait()" era utilizado para manter
# o terminal em execução enquanto a música estive-se tocando. Na versão recente
# não é mais possível usa-lo dessa forma. Existe diversas alternativas para ter
# o mesmo resultado, a escolhida foi a presente abaixo por ser a mais simples.
# 
# "pygame.mixer.music.get_busy()" verifica se existe algum áudio tocando.
# "while" mantém o áudio tocano e faz com que a verificação repita ENQUANTO o 
# áudio estiver tocando. Quando o áudio acabar o programa continua e finaliza.
while pygame.mixer.music.get_busy():
    print('A música está tocando...')
    sleep(1)

print('A música acabou.')
