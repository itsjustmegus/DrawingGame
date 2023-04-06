"""
    Name:    drawing_game.py
    Author:  Augustus Allred
    Created: 2/16/23
    Revised: 4/5/23
    Purpose: drawing software with pygame that allows user
             to click and drag to draw on screen
"""

# Import pygame library
import pygame
# Import sys.exit to cleanly exit program
from sys import exit

class DrawingGame:
# ----------------------------------------- INITIALIZE PYGAME ----------------------------------------- #
    def __init__(self):
        # Create drawing window
        self.WIDTH = 1000
        self.HEIGHT = 1000

        # Declare initial window and drawing color
        self.WINDOW_COLOR = 255, 255, 255
        self.DRAW_COLOR = "black"

        # Set Frames Per Second
        self.FPS = 120

        # Initialize pygame
        pygame.init()

        # Set caption for window
        pygame.display.set_caption("Gus' Doodle Board")

        # Load icon image for the window
        self.icon = pygame.image.load("./assets/draw_icon.png")
        # Set icon image for window
        pygame.display.set_icon(self.icon)
        
        # Create display window
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # The clock object manages how fast the game runs
        self.clock = pygame.time.Clock()

        # ------------------------- LOAD ASSETS ------------------------- #
        self.brush_size_img = pygame.image.load("./assets/brush_size.png").convert()
        self.size_1_img = pygame.image.load("./assets/size_1.png").convert()
        self.size_2_img = pygame.image.load("./assets/size_2.png").convert()
        self.size_3_img = pygame.image.load("./assets/size_3.png").convert()

# ----------------------------------------- GAME LOOP ----------------------------------------- #
    def run_game(self):
        "Draw background that doesn't update"
        # Fill the background with white
        self.SCREEN.fill(self.WINDOW_COLOR)
        """Infinite game loop"""
        while True:
            # Change in delta time for each frame
            # Multiplying movement by dt allows all computers
            # to run the game at the same speed
            # 120 frames per second
            self.dt = self.clock.tick(self.FPS)
            self.events()
            self.user_draw()
            self.draw_window()

# ----------------------------------------- EVENTS ----------------------------------------- #
    def events(self):
        """Listen for and handle program events"""
        for self.event in pygame.event.get():
            # Closing the program window
            # causes the QUIT event to be fired
            if self.event.type == pygame.QUIT:
                # Quit Pygame
                pygame.quit()
                # Exit Python
                exit()

# ---------------------------------------- USER DRAW --------------------------------------- #
    def user_draw(self):
        # Declare brush_size
        self.brush_size = 10

        # Get the mouse position
        self.px, self.py = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pressed()

        # Draw if the mouse is left clicked
        if self.mouse == (1,0,0): # left click
            # Draw a black rectangle where the cursor is with size 10px
            pygame.draw.rect(self.SCREEN, (self.DRAW_COLOR), (self.px, self.py, self.brush_size, self.brush_size))
            # Make the cursor invisible when drawing
            pygame.mouse.set_visible(False)

        # Erase if the mouse is right clicked
        if self.mouse == (0,0,1): # right click
            # Draw a rectangle with the same color
            # as the background where the cursor is with size 20px
            pygame.draw.rect(self.SCREEN, (self.WINDOW_COLOR), (self.px, self.py, 20, 20))
            # Make the cursor invisible when erasing

        if self.event.type == pygame.MOUSEBUTTONUP:
            self.press = False
            # Make the cursor visible when not drawing
            pygame.mouse.set_visible(True)

# --------------------------------------- DRAW SCREEN -------------------------------------- #
    def draw_window(self):
        # -------------------- DRAW brush_size BUTTON --------------------- #
        self.SCREEN.blit(self.brush_size_img, (100, 0))

        # ------------------ BUTTON CLICKED EVENTS -------------------- #
        # Add a portion where the game stops drawing if the mouse collides with the rect
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.brush_size_img.get_rect().collidepoint(100, 150):
                self.SCREEN.blit(self.size_1_img, (100, 128))
                self.SCREEN.blit(self.size_2_img, (100, 206))
                self.SCREEN.blit(self.size_3_img, (100, 284))
                # Does user click "close" button
                for self.event in pygame.event.get():
                    if self.event.type == pygame.QUIT:
                        running = False
                    if self.event.type == pygame.MOUSEBUTTONDOWN:
                        if self.size_1_img.get_rect().collidepoint(100, 128):
                            self.brush_size = 10
                        if self.size_2_img.get_rect().collidepoint(100, 206):
                            self.brush_size = 20
                        if self.size_3_img.get_rect().collidepoint(100, 284):
                            self.brush_size = 30


        # ------------- COPY BACKBUFFER INTO VIDEO MEMORY ------------- #
        # Redraw the screen
        pygame.display.update()


def main():
    # Initialize program object and start game
    drawing_game = DrawingGame()
    drawing_game.run_game()

if __name__ == "__main__":
    main()