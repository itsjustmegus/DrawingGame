"""
    Name:    wk6.py
    Author:  Augustus Allred
    Created: 2/16/23
    Purpose: First steps with pygame continued
"""

# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Create drawing window
WIDTH, HEIGHT = 1000, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Gus' Doodle Board")
icon = pygame.image.load("draw.png")
pygame.display.set_icon(icon)

WHITE = 255, 255, 255
DRAW_COLOR = "black"

FPS = 60

def draw_window():
    # Fill the background with white
        SCREEN.fill((WHITE))

def main():
    # Define clock object
    clock = pygame.time.Clock()
    # Create game loop that runs until user quits
    running = True

    while running:
        # Make game run at 60 FPS
        clock.tick(FPS)
        # Does user click "close" button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse = pygame.mouse.get_pressed()

        draw_window()

        # Get the mouse position
        px, py = pygame.mouse.get_pos()
        # If the mouse is pressed
        if mouse == (1,0,0): # left click
            # Draw a rectangle where the cursor is
            pygame.draw.rect(SCREEN, (DRAW_COLOR), (px,py,10,10))
        # If mouse is released
        if mouse == (0,0,1): # released
            # Stop drawing
            pygame.draw.rect(SCREEN, (WHITE), (px,py,10,10))

        # Flip display
        pygame.display.update()

    # Program finished
    pygame.quit()


if __name__ == "__main__":
    main()