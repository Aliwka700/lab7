import pygame
import time
import math


pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")


mickey_img = pygame.image.load(r"C:\Users\Айдана\Desktop\lab7\mickeyclock.jpeg")
mickey_img = pygame.transform.scale(mickey_img, (WIDTH, HEIGHT))


def draw_hand(angle, length, color, thickness):
    x = WIDTH // 2 + length * math.cos(math.radians(angle))
    y = HEIGHT // 2 - length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, (WIDTH // 2, HEIGHT // 2), (x, y), thickness)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(mickey_img, (0, 0))

  
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

 
    minute_angle = 90 - (minutes * 6)
    second_angle = 90 - (seconds * 6)

 
    draw_hand(minute_angle, 100, (0, 0, 255), 5)  
    draw_hand(second_angle, 120, (255, 0, 0), 3)  

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
