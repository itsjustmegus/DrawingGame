"""
    Name:    drawing_game.py
    Author:  Augustus Allred
    Created: 2/16/23
    Purpose: drawing software with pygame that allows user
             to click and drag to draw on screen
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

FPS = 120

def draw_window():
    # Fill the background with white
        SCREEN.fill((WHITE))

def main():
    # Define clock object
    clock = pygame.time.Clock()
    # Create game loop that runs until user quits
    running = True

    draw_window()

    while running:
        # Make game run at 120 FPS
        clock.tick(FPS)
        # Does user click "close" button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the mouse position
        mouse = pygame.mouse.get_pressed()
        px, py = pygame.mouse.get_pos()

        # If the mouse is pressed
        if mouse == (1,0,0): # left click
            # Draw a rectangle where the cursor is
            pygame.draw.rect(SCREEN, (DRAW_COLOR), (px,py,10,10))
            # Make the cursor invisible when drawing
            pygame.mouse.set_visible(False)

        if event.type == pygame.MOUSEBUTTONUP:
            press = False
            # Make the cursor visible when not drawing
            pygame.mouse.set_visible(True)
        

        # Flip display
        pygame.display.update()

    # Program finished
    pygame.quit()


if __name__ == "__main__":
    main()