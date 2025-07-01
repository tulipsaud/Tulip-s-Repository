import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0,125,255), pygame.Rect(30,30,60,60))
    pygame.display.flip()
pygame.init()
sw, sh = 300, 300
display_surface = pygame.display.set_mode((sw, sh))
background_image = pygame.trasnform.scale(
    pygame.image.load('background.png').convert(),
    (sw, sh))
penguin_image = pygame.transform.scale(
    pygame.image.load('butterfly.png').convert_alpha(), (250, 250))
penguin_rect = penguin_image.get_rect(center=(sw//2,
                                              sh//2 - 30))
text = pygame.font.Font(None,36).render('Hello World', True , pygame.Color('black'))
text_rect = text.get_rect(center=(sw//2, sh // 2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)
         
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()



