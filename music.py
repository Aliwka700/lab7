import pygame
import os

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Список музыкальных файлов
music_files = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_track = 0
pygame.mixer.music.load(music_files[current_track])

# Окно
WIDTH, HEIGHT = 300, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:  # Play
        pygame.mixer.music.play()
    if keys[pygame.K_s]:  # Stop
        pygame.mixer.music.stop()
    if keys[pygame.K_n]:  # Next track
        current_track = (current_track + 1) % len(music_files)
        pygame.mixer.music.load(music_files[current_track])
        pygame.mixer.music.play()
    if keys[pygame.K_b]:  # Previous track
        current_track = (current_track - 1) % len(music_files)
        pygame.mixer.music.load(music_files[current_track])
        pygame.mixer.music.play()
    
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
