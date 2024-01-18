import pygame
pygame.init()
pygame.mixer.music.load('Magika.mp3')
pygame.mixer.music.play()
pygame.mixer.music.queue('ex021.mp3')
res = str(input('Quer pular? [S/N]')).upper()
if res == 'S':
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()
input()
pygame.event.wait()
