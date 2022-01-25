#!usr/bin/env python3
import sys
import pygame

FPS = 60

DISPLAY_WIDTH = 750
DISPLAY_HEIGHT = 60

NOTE_FONT = None
NOTE_FONT_SIZE = 32

BACKGROUND_RECT_X = 0
BACKGROUND_RECT_Y = 0
BACKGROUND_RECT_COLOR = (60, 60, 60)

BLACK_COLOR = (0, 0, 0)

TEXT_START_OFFSET_X = 15
TEXT_START_OFFSET_Y = 15

TEXT_COLOR = (200, 200, 200)

BACKSPACE_NEXT_DELETE_TIME = 0
BACKSPACE_DELETE_INTERVAL_DELAY = 50


def GetNoteText():
    "Create text box for the user input. Save the user input."
    global BACKSPACE_NEXT_DELETE_TIME
    global BACKSPACE_DELETE_INTERVAL_DELAY
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode(
        [DISPLAY_WIDTH, DISPLAY_HEIGHT],
        pygame.NOFRAME,
        vsync=1
    )
    background_rect = pygame.Rect(
        BACKGROUND_RECT_X,
        BACKGROUND_RECT_Y,
        DISPLAY_WIDTH,
        DISPLAY_HEIGHT
    )

    font = pygame.font.Font(NOTE_FONT, NOTE_FONT_SIZE)

    text = ''
    input_box_pointed = True

    shift_down = False
    backspace_down = False

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                input_box_pointed = background_rect.collidepoint(event.pos)

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LSHIFT
                    or event.key == pygame.K_RSHIFT):
                    shift_down = True

                if event.key == pygame.K_BACKSPACE:
                    backspace_down = True
                elif event.key == pygame.K_RETURN:
                    if shift_down and input_box_pointed:
                        text += "\n"
                    else:
                        done = True
                else:
                    if input_box_pointed:
                        text += event.unicode

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LSHIFT
                    or event.key == pygame.K_RSHIFT):
                    shift_down = False
                if event.key == pygame.K_BACKSPACE:
                    backspace_down = False

        if backspace_down and (pygame.time.get_ticks() > BACKSPACE_NEXT_DELETE_TIME):
            text = text[:-1]
            BACKSPACE_NEXT_DELETE_TIME = pygame.time.get_ticks() + BACKSPACE_DELETE_INTERVAL_DELAY

        if not backspace_down:
            BACKSPACE_NEXT_DELETE_TIME = pygame.time.get_ticks()

        display.fill(BLACK_COLOR)
        pygame.draw.rect(display, BACKGROUND_RECT_COLOR, background_rect)
        text_surface = font.render(text, True, TEXT_COLOR)
        display.blit(
            text_surface,
            (
                background_rect.x + TEXT_START_OFFSET_X,
                background_rect.y + TEXT_START_OFFSET_Y
             )
        )

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

    return text
