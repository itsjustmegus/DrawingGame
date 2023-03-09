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
icon = pygame.image.load("images\draw.png")
pygame.display.set_icon(icon)

WINDOW_COLOR = 255, 255, 255
DRAW_COLOR = "black"

FPS = 120

def draw_window():
    # Fill the background with white
    SCREEN.fill(WINDOW_COLOR)

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
        px, py = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        # Draw if the mouse is left clicked
        if mouse == (1,0,0): # left click
            # Draw a black rectangle where the cursor is with size 10px
            pygame.draw.rect(SCREEN, (DRAW_COLOR), (px,py,10,10))
            # Make the cursor invisible when drawing
            pygame.mouse.set_visible(False)

        # Erase if the mouse is right clicked
        if mouse == (0,0,1): # right click
            # Draw a rectangle with the same color
            # as the background where the cursor is with size 20px
            pygame.draw.rect(SCREEN, (WINDOW_COLOR), (px,py,20,20))
            # Make the cursor invisible when erasing

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