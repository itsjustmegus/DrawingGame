import pygame
from collections import deque

class DrawEntity:
    def __init__(self):
        self.entity = []

    def add(self, toAdd):
        self.entity.append(toAdd)

    def remove(self):
        self.entity = []

    def __str__(self):
        return ' '.join(map(str, self.entity))

DrawEnt = deque()

def draw(window):
    if len(DrawEnt) > 0:
        d_Ent = DrawEnt[-1]

        mouseX, mouseY = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0]:
            rect = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(mouseX, mouseY, 3, 3), 3)
            d_Ent.add(rect)

def main():

    running = True
    window = pygame.display.set_mode((640, 480))
    window.fill((255, 255, 255))


    while running:
        clock.tick(3200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                d_Ent = DrawEntity()
                DrawEnt.append(DrawEntity())

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_LCTRL:

                    if len(DrawEnt) > 0:
                        DrawEnt.pop()
                        window.fill((255, 255, 255))
                        for entity in DrawEnt:
                            for r in entity.entity:
                                pygame.draw.rect(window, (0, 0, 0), r, 3)

            draw(window)

        pygame.display.flip()
    #end main loop
    pygame.quit()

if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()
    main()
