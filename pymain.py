import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pathfinding Algorithms Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Menu options
menu_options = ["Run Algorithm 1", "Run Algorithm 2", "Run Algorithm 3", "Exit"]
selected_option = 0

# Function to draw the menu
def draw_menu():
    screen.fill(WHITE)
    for index, option in enumerate(menu_options):
        color = BLUE if index == selected_option else BLACK
        text = font.render(option, True, color)
        text_rect = text.get_rect(center=(screen_width // 2, 150 + index * 50))
        screen.blit(text, text_rect)
    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if selected_option == len(menu_options) - 1:  # Exit option
                    running = False
                else:
                    print(f"Selected: {menu_options[selected_option]}")  # Placeholder for algorithm execution

    draw_menu()

pygame.quit()
sys.exit()
