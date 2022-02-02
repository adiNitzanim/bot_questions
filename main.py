import pygame

from Question import Question
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, CHAT_WINDOW_WIDTH, \
    CHAT_WINDOW_HEIGHT, CHAT_WINDOW_X, CHAT_WINDOW_Y
from helpers import screen


def main():
    # Set up the game display, clock and headline
    pygame.init()
    # pygame.mixer.init()
    # pygame.mixer.music.load('music/background_music.mp3')
    # pygame.mixer.music.play(0)

    # Change the title of the window
    pygame.display.set_caption('Future teller')

    clock = pygame.time.Clock()

    # Set up background image
    chat_background = pygame.image.load('images/chat_background.jpg')
    chat_background = pygame.transform.scale(chat_background,
                                             (CHAT_WINDOW_WIDTH, CHAT_WINDOW_HEIGHT))
    background = pygame.image.load('images/background.jpg')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    question = Question(1, "a lot of word in this question, will the text will "
                        "slice as i want? i dont know lets hope so, if not im "
                        "gonna be very very sad", ["1","2","3","4"])
    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position (x,y) of the mouse press
                pass

        # Update display - without input update everything
        screen.blit(chat_background, (CHAT_WINDOW_X, CHAT_WINDOW_Y))
        screen.blit(background, (0, 0))
        question.display_question()
        question.display_answers()

        # display_ask_question(screen, zulu_answer, 90, (255, 0, 0))
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()

main()
