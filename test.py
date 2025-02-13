import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy Valentines Day!")

font = pygame.font.Font(None, 35)
hidden_text = "Will you be my Valentine?"

text_surface = font.render(hidden_text, True, (255, 0, 0))  
text_rect = text_surface.get_rect(center=(width // 2, height // 2))

yes_rect = pygame.Rect(250, 400, 120, 50)  
no_rect = pygame.Rect(450, 400, 120, 50)   
button_font = pygame.font.Font(None, 40)

running = True
clock = pygame.time.Clock()

def get_random_position(exclude_rect):
    while True:
        x = random.randint(50, width - no_rect.width - 50)
        y = random.randint(350, height - no_rect.height - 50)
        random_rect = pygame.Rect(x, y, no_rect.width, no_rect.height)
        if not exclude_rect.colliderect(random_rect):
            return x, y

while running:
    screen.fill((0, 0, 0))  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        if running:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if no_rect.collidepoint(event.pos):
                    new_size = max(20, no_rect.width - 20)
                    no_rect.size = (new_size, new_size)
                    no_rect.x, no_rect.y = get_random_position(yes_rect)

                if yes_rect.collidepoint(event.pos):
                    print("Thanks for accepting my praposal! 😍❤️💕")
                    running = False
    mouse_x, mouse_y = pygame.mouse.get_pos()

    torch_surface = pygame.Surface((width, height))
    torch_surface.fill((0, 0, 0))
    pygame.draw.circle(torch_surface, (255, 255, 255), (mouse_x, mouse_y), 100)
    torch_surface.set_colorkey((255, 255, 255))

    if running:
        pygame.draw.rect(screen, (0, 0, 0), yes_rect)
        pygame.draw.rect(screen, (0, 0, 0), no_rect)
        
        yes_text = button_font.render("Yes", True, (255, 255, 255))
        no_text = button_font.render("No", True, (255, 255, 255))
        screen.blit(yes_text, (yes_rect.x + 30, yes_rect.y + 10))
        screen.blit(no_text, (no_rect.x + 5, no_rect.y + 5)) 

    screen.blit(text_surface, text_rect)
    screen.blit(torch_surface, (0, 0))

    pygame.display.flip()
    clock.tick(100)

pygame.quit()
