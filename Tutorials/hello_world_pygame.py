"""
    Name:    hello_world_pygame.py
    Author:  Augustus Allred
    Created: 2/16/23
    Purpose: First steps with pygame
"""

# Import pygame library
import pygame
# Initialize pygame
pygame.init()

# Create drawing window
screen = pygame.display.set_mode((500, 500))

# Create game loop that runs until user quits
running = True

while running:
    # Does user click "close" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw blue circle in center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip display
    pygame.display.flip()

# Program finished
pygame.quit()