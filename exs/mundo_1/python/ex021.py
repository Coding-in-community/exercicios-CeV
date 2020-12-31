"""
Desafio 021

Problema: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

Resolução do problema:
"""
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
