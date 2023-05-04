"""
    Name: beat_maker_10.py
    Author:
    Date:
    Purpose: Add save and load menus
"""
# pip install pygame
from matplotlib.ft2font import LOAD_TARGET_MONO
import pygame

# Initialize pygame
pygame.init()

# Color Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (170, 170, 170)
GRAY = (128, 128, 128)
DARK_GRAY = (50, 50, 50)
GREEN = (0, 255, 0)
GOLD = (212, 175, 55)
NEON_BLUE = (0, 255, 255)

WIDTH = 1400
HEIGHT = 800

# Create screen, set caption
SCREEN = pygame.display.set_mode(
    [WIDTH, HEIGHT]
)
pygame.display.set_caption("Beat Maker")
pygame_icon = pygame.image.load("drums.png")
pygame.display.set_icon(pygame_icon)

# This font is always available in system
# label_font = pygame.font.Font("freesansbold.ttf")
# A free font from the internet
medium_font = pygame.font.Font("Roboto-Bold.ttf", 24)
label_font = pygame.font.Font("Roboto-Bold.ttf", 32)
# Set 60 frames per second
FPS = 60
# Create clock object
clock = pygame.time.Clock()

# Beats per measure
beats = 8
# How many instruments in menu
instruments = 6
# Initialize a lists of lists = -1
# to store which beat box and instrument are active 1, inactive -1
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
# List of active instruments, all enabled
active_instruments = [1 for _ in range(instruments)]

# beats per minute
bpm = 240
# Use to pause and start the drum machine
playing = True
active_length = 0
active_beat = 0
beat_changed = True
save_menu = False
load_menu = False
saved_beats = []
index = 0
file = open("saved_beats.txt", "r")
for line in file:
    saved_beats.append(line)
beat_name = ""
typing = False

# Load sounds
hi_hat = pygame.mixer.Sound("sounds\hi_hat.wav")
snare = pygame.mixer.Sound("sounds\snare.wav")
kick = pygame.mixer.Sound("sounds\kick.wav")
crash = pygame.mixer.Sound("sounds\crash.wav")
clap = pygame.mixer.Sound("sounds\clap.wav")
tom = pygame.mixer.Sound("sounds\\tom.wav")
# Set 3 channels per instruments
pygame.mixer.set_num_channels(instruments * 3)


# ------------------------- PLAY NOTES ------------------------------------#
def play_notes():
    # Go through each item in the instrument list
    for i in range(len(clicked)):
        # If the instrument is active
        if clicked[i][active_beat] == 1 and active_instruments[i] == 1:
            if i == 0:
                hi_hat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                crash.play()
            if i == 4:
                clap.play()
            if i == 5:
                tom.play()


# ------------------------- DRAW GRID -------------------------------------#
def draw_grid(clicked, active_beat, active_instruments):
    # Draw a hollow rectangle to the surface for left menu
    left_menu = pygame.draw.rect(
        SCREEN,                   # Drawing surface
        GRAY,                     # Drawing color
        [
            0,                    # x coordinate
            0,                    # y coordinate
            200,                  # width
            HEIGHT - 200   # height
        ],
        width=5                 # width > 0, rectangle line thickness
    )

    # Draw a hollow rectangle to the surface for bottom menu
    bottom_menu = pygame.draw.rect(
        SCREEN,                   # Drawing surface
        GRAY,                     # Drawing color
        [
            0,                    # x coordinate
            HEIGHT - 200,  # y coordinate
            WIDTH,         # width
            200                   # height
        ],
        width=5                 # width > 0, rectangle line thickness
    )

    # Create a list for the beat boxes
    boxes = []
    colors = [GRAY, WHITE, GRAY]

    # Create and draw instrument text in left menu
    hi_hat_text = label_font.render(
        "Hi Hat", True,
        # active instruments is either -1 or 1
        # this is the last item, or the number 1 item in colors list
        colors[active_instruments[0]]
    )
    SCREEN.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render(
        "Snare", True, colors[active_instruments[1]])
    SCREEN.blit(snare_text, (30, 130))
    bass_drum_text = label_font.render(
        "Bass Drum", True, colors[active_instruments[2]])
    SCREEN.blit(bass_drum_text, (30, 230))
    crash_text = label_font.render(
        "Crash", True, colors[active_instruments[3]])
    SCREEN.blit(crash_text, (30, 330))
    clap_text = label_font.render("Clap", True, colors[active_instruments[4]])
    SCREEN.blit(clap_text, (30, 430))
    floor_tom_text = label_font.render(
        "Floor Tom", True, colors[active_instruments[5]])
    SCREEN.blit(floor_tom_text, (30, 530))

    # Draw horizontal lines between menu items
    for i in range(1, instruments):
        pygame.draw.line(
            SCREEN,          # Drawing surface
            GRAY,            # Drawing color
            (0, i * 100),    # Beginning point
            (200, i * 100),  # Ending point
            width=3        # Line width
        )

    # Draw grid of beat boxes
    for i in range(beats):
        for j in range(instruments):
            # j is row, i is column
            # -1 indicates the box is not clicked
            if clicked[j][i] == -1:
                color = GRAY
            else:
                if active_instruments[j] == 1:
                    color = GREEN
                else:
                    color = DARK_GRAY

            # Draw solid rectangles that change color
            # GRAY inactive, GREEN active
            rect = pygame.draw.rect(
                SCREEN,
                color,
                [
                    # // floor division ensures integer spacing
                    i * ((WIDTH - 200) // beats) + 205,   # x coordinate
                    (j * 100) + 5,                              # y coordinate
                    ((WIDTH - 200) // beats) - 10,             # width
                    ((HEIGHT - 200) // instruments) - 10       # height
                ],
                width=0,         # Line width = 0 fill the rectangle
                border_radius=3  # Radius of rounded corners
            )

            # Draw a gold border around the rectangles
            pygame.draw.rect(
                SCREEN,
                GOLD,
                [
                    # // floor division ensures integer spacing
                    i * ((WIDTH - 200) // beats) + 200,   # x coordinate
                    j * 100,                                     # y coordinate
                    ((WIDTH - 200) // beats),             # width
                    ((HEIGHT - 200) // instruments)       # height
                ],
                width=5,         # width > 0, rectangle line thickness
                border_radius=5  # Radius of rounded corners
            )

            # Draw black lines between each rectangle
            pygame.draw.rect(
                SCREEN,
                BLACK,
                [
                    # // floor division ensures integer spacing
                    i * ((WIDTH - 200) // beats) + 200,   # x coordinate
                    j * 100,                                     # y coordinate
                    ((WIDTH - 200) // beats),             # width
                    ((HEIGHT - 200) // instruments)       # height
                ],
                width=2,         # width > 0, rectangle line thickness
                border_radius=5  # Radius of rounded corners
            )

            # Update list that tracks each rect state and location
            boxes.append(
                (rect,        # Track each rect for collision detection
                    (i, j)    # Track each rect x, y location in grid
                 ))

            # Display the active beat
            active = pygame.draw.rect(
                SCREEN,
                NEON_BLUE,
                [
                    active_beat * (
                        (WIDTH - 200) // beats) + 200,  # x coordinate
                    0,                                         # y coordinate
                    ((WIDTH - 200) // beats),           # width
                    instruments * 100                          # height
                ],
                width=5,         # width > 0, rectangle line thickness
                border_radius=5  # Radius of rounded corners
            )

    return boxes


# ------------------------- DRAW SAVE MENU --------------------------------#
def draw_save_menu(beat_name, typing):
    # Draw surface for menu
    pygame.draw.rect(SCREEN, BLACK, [0, 0, WIDTH, HEIGHT])
    # Menu text to describe menu
    menu_text = label_font.render(
        "SAVE MENU: Enter a Name for the Current Beat:", True, WHITE)
    SCREEN.blit(menu_text, (400, 40))

    # Create and draw save button
    save_btn = pygame.draw.rect(
        SCREEN, GRAY, [WIDTH // 2 - 200, HEIGHT * 0.75, 400, 100], 0, 5)
    save_txt = label_font.render("Save Beat", True, WHITE)
    SCREEN.blit(save_txt, (WIDTH // 2 - 70, HEIGHT * 0.75 + 30))

    # Indicate that we are typing
    if typing:
        pygame.draw.rect(SCREEN, DARK_GRAY, [400, 200, 600, 200], 0, 5)

    # Entry rectangle
    entry_rect = pygame.draw.rect(SCREEN, GRAY, [400, 200, 600, 200], 5, 5)
    entry_text = label_font.render(f"{beat_name}", True, WHITE)
    SCREEN.blit(entry_text, (430, 250))

    # Close button
    close_btn = pygame.draw.rect(
        SCREEN, GRAY, [WIDTH-200, HEIGHT - 100, 180, 90], 0, 5)
    exit_text = label_font.render("Close", True, WHITE)
    SCREEN.blit(exit_text, (WIDTH - 160, HEIGHT - 70))

    return close_btn, save_btn, entry_rect


# ------------------------- DRAW LOAD MENU --------------------------------#
def draw_load_menu(index):
    loaded_clicked = []
    loaded_beats = 0
    loaded_bpm = 0
    # Draw surface for menu
    pygame.draw.rect(SCREEN, BLACK, [0, 0, WIDTH, HEIGHT])

    # Menu text to describe menu
    menu_text = label_font.render(
        "LOAD MENU: Select a Beat to Load:", True, WHITE)
    SCREEN.blit(menu_text, (400, 40))

    # Load button
    load_btn = pygame.draw.rect(
        SCREEN, GRAY, [(WIDTH // 2) - 200, HEIGHT * 0.87, 400, 100], 0, 5)
    load_txt = label_font.render("Load Beat", True, WHITE)
    SCREEN.blit(load_txt, ((WIDTH // 2) - 70, HEIGHT * 0.87 + 30))

    # Delete button
    delete_btn = pygame.draw.rect(
        SCREEN, GRAY, [(WIDTH // 2) - 500, HEIGHT * 0.87, 200, 100], 0, 5)
    delete_txt = label_font.render("Delete Beat", True, WHITE)
    SCREEN.blit(delete_txt, (WIDTH // 2 - 475, (HEIGHT * 0.87 + 30)))

    # Draw close button to leave menu
    close_btn = pygame.draw.rect(
        SCREEN, GRAY, [WIDTH-200, HEIGHT - 100, 180, 90], 0, 5)
    exit_text = label_font.render("Close", True, WHITE)
    SCREEN.blit(exit_text, (WIDTH - 160, HEIGHT - 70))

    # Display file names
    loaded_rectangle = pygame.draw.rect(
        SCREEN, GRAY, [190, 90, 1000, 600], 5, 5)

    if 0 <= index < len(saved_beats):
        pygame.draw.rect(
            SCREEN, LIGHT_GRAY, [190, 100 + index * 50, 1000, 50])

    # Display saved beats
    for beat in range(len(saved_beats)):
        if beat < 10:
            beat_clicked = []
            row_text = medium_font.render(f"{beat + 1}", True, WHITE)
            SCREEN.blit(row_text, (200, 100 + (beat * 50)))
            name_index_start = saved_beats[beat].index("name: ") + 6
            name_index_end = saved_beats[beat].index(", beats")
            name_text = medium_font.render(
                saved_beats[beat][name_index_start:name_index_end],
                True, WHITE)
            SCREEN.blit(name_text, (240, 100 + (beat * 50)))

        # Check if we have selected a beat
        if 0 <= index < len(saved_beats) and beat == index:
            beats_index_end = saved_beats[beat].index(', bpm:')
            loaded_beats = int(
                saved_beats[beat][name_index_end + 8:beats_index_end])
            bpm_index_end = saved_beats[beat].index(', selected:')
            loaded_bpm = int(saved_beats[beat]
                             [beats_index_end + 6:bpm_index_end])
            loaded_clicks_string = saved_beats[beat][bpm_index_end + 14: -3]
            loaded_clicks_rows = list(loaded_clicks_string.split("], ["))
            for row in range(len(loaded_clicks_rows)):
                loaded_clicks_row = loaded_clicks_rows[row].split(", ")
                for item in range(len(loaded_clicks_row)):
                    if loaded_clicks_row[item] == "1" or loaded_clicks_row[item] == "-1":
                        loaded_clicks_row[item] = int(loaded_clicks_row[item])
                beat_clicked.append(loaded_clicks_row)
                loaded_clicked = beat_clicked

    loaded_info = [loaded_beats, loaded_bpm, loaded_clicked]

    return close_btn, load_btn, delete_btn, loaded_rectangle, loaded_info


# ------------------------- GAME LOOP -------------------------------------#
run = True
while run:
    # Clear the screen to black
    SCREEN.fill(BLACK)

    # Draw the grid colors based on whether the box is active or not
    boxes = draw_grid(clicked, active_beat, active_instruments)

    # Play pause button
    play_pause = pygame.draw.rect(
        SCREEN, GRAY,
        [50, HEIGHT - 150, 200, 100],
        0, 5)
    play_text = label_font.render("Play/Pause", True, WHITE)
    SCREEN.blit(play_text, (70, HEIGHT - 140))
    if playing:
        play_text2 = medium_font.render("Playing", True, DARK_GRAY)
    else:
        play_text2 = medium_font.render("Paused", True, DARK_GRAY)
    SCREEN.blit(play_text2, (70, HEIGHT - 100))

    # bpm stuff
    bpm_rect = pygame.draw.rect(
        SCREEN, GRAY, [300, HEIGHT - 150, 200, 100], 5, 5)
    bpm_text = medium_font.render("Beats Per Minute", True, WHITE)
    SCREEN.blit(bpm_text, (308, HEIGHT - 130))
    bpm_text2 = label_font.render(f"{bpm}", True, WHITE)
    SCREEN.blit(bpm_text2, (370, HEIGHT - 100))
    # Buttons to change bpm by 5
    bpm_add_rect = pygame.draw.rect(
        SCREEN, GRAY, [510, HEIGHT - 150, 48, 48], 0, 5)
    bpm_sub_rect = pygame.draw.rect(
        SCREEN, GRAY, [510, HEIGHT - 100, 48, 48], 0, 5)
    add_text = medium_font.render("+5", True, WHITE)
    sub_text = medium_font.render("-5", True, WHITE)
    SCREEN.blit(add_text, (520, HEIGHT - 140))
    SCREEN.blit(sub_text, (520, HEIGHT - 90))

    # beats stuff
    beats_rect = pygame.draw.rect(
        SCREEN, GRAY, [600, HEIGHT - 150, 200, 100], 5, 5)
    beats_text = medium_font.render("Beats in Loop", True, WHITE)
    SCREEN.blit(beats_text, (618, HEIGHT - 130))
    beats_text2 = label_font.render(f"{beats}", True, WHITE)
    SCREEN.blit(beats_text2, (680, HEIGHT - 100))
    # Buttons to change beats in loop
    beats_add_rect = pygame.draw.rect(
        SCREEN, GRAY, [810, HEIGHT - 150, 48, 48], 0, 5)
    beats_sub_rect = pygame.draw.rect(
        SCREEN, GRAY, [810, HEIGHT - 100, 48, 48], 0, 5)
    add_text2 = medium_font.render("+1", True, WHITE)
    sub_text2 = medium_font.render("-1", True, WHITE)
    SCREEN.blit(add_text2, (820, HEIGHT - 140))
    SCREEN.blit(sub_text2, (820, HEIGHT - 90))

    # Instrument rects
    instrument_rects = []
    # We will only create these rects, but not display them
    # Use for collision detection with the mouse to turn
    # the instruments off and on
    for i in range(instruments):
        rect = pygame.rect.Rect((0, i * 100), (200, 100))
        instrument_rects.append(rect)

    # --------------------DRAW SAVE LOAD BEATS BUTTONS --------------------#
    # Save and load drum beats buttons
    save_button = pygame.draw.rect(
        SCREEN, GRAY, [900, HEIGHT - 150, 200, 48], 0, 5)
    save_text = label_font.render("Save Beat", True, WHITE)
    SCREEN.blit(save_text, (920, HEIGHT - 145))

    load_button = pygame.draw.rect(
        SCREEN, GRAY, [900, HEIGHT - 100, 200, 48], 0, 5)
    load_text = label_font.render("Load Beat", True, WHITE)
    SCREEN.blit(load_text, (920, HEIGHT - 95))

    # --------------------------- CLEAR BOARD ----------------------------#
    clear_button = pygame.draw.rect(
        SCREEN, GRAY, [1150, HEIGHT - 150, 200, 100], 0, 5)
    clear_text = label_font.render("Clear", True, WHITE)
    SCREEN.blit(clear_text, (1160, HEIGHT - 130))

    if save_menu:
        exit_button, save_button, entry_rectangle = draw_save_menu(
            beat_name, typing)
    if load_menu:
        exit_button, load_button, delete_button, loaded_rectangle, loaded_info = draw_load_menu(
            index)

    if beat_changed:
        play_notes()
        beat_changed = False

    # Capture all game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit loop
            run = False
        # Watch for mouse button down clicks
        if event.type == pygame.MOUSEBUTTONDOWN and not save_menu and not load_menu:
            # Test for which rect was clicked
            for i in range(len(boxes)):
                # if a box has been clicked
                # event.pos is the position of the mouse
                if boxes[i][0].collidepoint(event.pos):
                    # Get the coordinates of the clicked box
                    coords = boxes[i][1]
                    # Set the clicked rect active or inactive
                    clicked[coords[1]][coords[0]] *= -1
        # Use mouse button up to not have bounces
        if event.type == pygame.MOUSEBUTTONUP and not save_menu and not load_menu:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True
            # Increase or decrease bpm by 5
            elif bpm_add_rect.collidepoint(event.pos):
                bpm += 5
            elif bpm_sub_rect.collidepoint(event.pos):
                bpm -= 5
            # Clear board
            elif clear_button.collidepoint(event.pos):
                clicked = [[-1 for _ in range(beats)]
                           for _ in range(instruments)]
            # Increase or decrease beats per loop
            elif beats_add_rect.collidepoint(event.pos):
                beats += 1
            # Go through each row and add an item at the end
                for i in range(len(clicked)):
                    clicked[i].append(-1)
            elif beats_sub_rect.collidepoint(event.pos):
                beats -= 1
                # Go through each row and pop off the last item
                for i in range(len(clicked)):
                    clicked[i].pop(-1)

            elif save_button.collidepoint(event.pos):
                save_menu = True
            elif load_button.collidepoint(event.pos):
                load_menu = True

            for i in range(len(instrument_rects)):
                if instrument_rects[i].collidepoint(event.pos):
                    # Enable or disable instrument
                    active_instruments[i] *= -1

        elif event.type == pygame.MOUSEBUTTONUP:
            # Close save menu
            if exit_button.collidepoint(event.pos):
                save_menu = False
                load_menu = False
                playing = True
                beat_name = ""
                typing = False

            if load_menu:
                if loaded_rectangle.collidepoint(event.pos):
                    index = (event.pos[1] - 100) // 50

                if delete_button.collidepoint(event.pos):
                    if 0 <= index < len(saved_beats):
                        saved_beats.pop(index)

                if load_button.collidepoint(event.pos):
                    beats = loaded_info[0]
                    bpm = loaded_info[1]
                    clicked = loaded_info[2]
                    index = 100
                    load_menu = False

            if save_menu:

                # Enter file name
                if entry_rectangle.collidepoint(event.pos):
                    if typing:
                        typing = False
                    elif not typing:
                        typing = True

                # Save beat to file
                if save_button.collidepoint(event.pos):
                    file = open("saved_beats.txt", "w")
                    saved_beats.append(
                        f"\nname: {beat_name}, beats: {beats}, bpm: {bpm}, selected: {clicked}")
                    for i in range(len(saved_beats)):
                        file.write(str(saved_beats[i]))
                    file.close()
                    save_menu = False
                    typing = False
                    beat_name = ""

        # If typing is true and we are typing
        # text will go into the text area
        if event.type == pygame.TEXTINPUT and typing:
            # Every key stroke is an event.text
            beat_name += event.text

        if event.type == pygame.KEYDOWN:
            # Do not allow backspace if beat_name is empty
            if event.key == pygame.K_BACKSPACE and len(beat_name) > 0 and typing:
                # Remove the last character
                beat_name = beat_name[:-1]

    # 3600 is how many fps in a minute
    # Divide by bpm to give beat_length
    beat_length = 3600 // bpm

    if playing:
        # active_length tracks what beat we are on in the measure
        if active_length < beat_length:
            active_length += 1
        # Reset as we are starting a new measure
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

    # Update the display
    pygame.display.update()
    # Game loop processes 60 times a second
    clock.tick(FPS)

pygame.quit()
exit()
