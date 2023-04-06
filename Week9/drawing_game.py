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

# --------------------------------------- DRAW SCREEN -------------------------------------- #
    def draw_window(self):
        # Redraw the screen
        pygame.display.update()

# ---------------------------------------- USER DRAW --------------------------------------- #
    def user_draw(self):
        # Get the mouse position
        self.px, self.py = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pressed()

        # Draw if the mouse is left clicked
        if self.mouse == (1,0,0): # left click
            # Draw a black rectangle where the cursor is with size 10px
            pygame.draw.rect(self.SCREEN, (self.DRAW_COLOR), (self.px,self.py,10,10))
            # Make the cursor invisible when drawing
            pygame.mouse.set_visible(False)

        # Erase if the mouse is right clicked
        if self.mouse == (0,0,1): # right click
            # Draw a rectangle with the same color
            # as the background where the cursor is with size 20px
            pygame.draw.rect(self.SCREEN, (self.WINDOW_COLOR), (self.px,self.py,20,20))
            # Make the cursor invisible when erasing

        if self.event.type == pygame.MOUSEBUTTONUP:
            self.press = False
            # Make the cursor visible when not drawing
            pygame.mouse.set_visible(True)


def main():
    # Initialize program object and start game
    drawing_game = DrawingGame()
    drawing_game.run_game()

if __name__ == "__main__":
    main()


"""# -------------------- DRAW REPLAY BUTTON --------------------- #
replay_btn = pygame.draw.rect(
    self.screen,
    "black",
    [self.WIDTH // 2 - 100, self.HEIGHT // 2 + 50, 80, 30],
    0,
    border_radius = 5
)
replay_txt = self.font_small.render(" Replay", True, "white")
self.screen.blit(
    replay_txt,
    (
        self.WIDTH // 2 - 100,
        self.HEIGHT // 2 + 50
    )
)"""