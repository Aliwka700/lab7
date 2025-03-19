import pygame
import time
import math
from datetime import datetime


pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")


clock_img = pygame.image.load("clock.png") 
minute_hand = pygame.image.load("right_hand.png")  
second_hand = pygame.image.load("left_hand.png")    


center_x, center_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    screen.fill((255, 255, 255)) 
    screen.blit(clock_img, (0, 0))  
    
   
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    
   
    minute_angle = -(minutes * 6)  
    second_angle = -(seconds * 6)  
    
    
    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)
    
    
    screen.blit(rotated_minute, rotated_minute.get_rect(center=(center_x, center_y)))
    screen.blit(rotated_second, rotated_second.get_rect(center=(center_x, center_y)))
    
    pygame.display.flip()  
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    time.sleep(1) 

pygame.quit()





