from PIL import Image
import pygame
import glob
import os

pygame.init()

size = width, height = 600, 400

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Trace")
clock = pygame.time.Clock()

loop = True
press = False
color = "white"
count = 0
[os.remove(png) for png in glob.glob("*png")]

while loop:
    try:
        # pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if count < 10:
                        pygame.image.save(screen, f"screenshot0{count}.png")
                    else:
                        pygame.image.save(screen, f"screenshot{count}.png")
                    count += 1
                if event.key == pygame.K_g:
                        frames = []
                        imgs = glob.glob("*.png")
                        for i in imgs:
                            new_frame = Image.open(i)
                            frames.append(new_frame)

                        # Save into a GIF file that loops forever
                        frames[0].save('animated.gif', format='GIF',
                                        append_images=frames[1:],
                                        save_all=True,
                                        duration=300, loop=0)
                        os.startfile("animated.gif")

        px, py = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1,0,0):
            pygame.draw.rect(screen, (color), (px,py,10,10))
        if pygame.mouse.get_pressed() == (0,0,1):
            pygame.draw.rect(screen, (0,0,0), (px,py,10,10))

        if event.type == pygame.MOUSEBUTTONUP:
            press = False
        pygame.display.update()
        clock.tick(1000)
    except Exception as e:
        print(e)
        pygame.quit()

pygame.quit()