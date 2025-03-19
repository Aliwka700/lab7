import pygame


pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")


ball = pygame.Rect(225, 225, 50, 50)
ball_speed = 20

running = True
while running:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball.y > 0:
        ball.y -= ball_speed
    if keys[pygame.K_DOWN] and ball.y < HEIGHT - ball.height:
        ball.y += ball_speed
    if keys[pygame.K_LEFT] and ball.x > 0:
        ball.x -= ball_speed
    if keys[pygame.K_RIGHT] and ball.x < WIDTH - ball.width:
        ball.x += ball_speed
    
    pygame.draw.circle(screen, (255, 0, 0), (ball.x + 25, ball.y + 25), 25)
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
