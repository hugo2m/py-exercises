import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("ex021-040/ex021.mp3")
pygame.mixer.music.play()

# Mantém o programa ativo enquanto o som toca
while pygame.mixer.music.get_busy():
    time.sleep(1)