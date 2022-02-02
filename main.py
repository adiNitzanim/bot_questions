import pygame

from Question import Question
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, CHAT_WINDOW_WIDTH, \
    CHAT_WINDOW_HEIGHT, CHAT_WINDOW_X, CHAT_WINDOW_Y, NUM_OF_QUESTIONS
from database_functions import analyze_data
from helpers import screen, mouse_in_button


def main():
    # Set up the game display, clock and headline
    pygame.init()
    # pygame.mixer.init()
    # pygame.mixer.music.load('music/background_music.mp3')
    # pygame.mixer.music.play(0)

    # Change the title of the window
    pygame.display.set_caption('Future teller')

    clock = pygame.time.Clock()

    background = pygame.image.load('images/background.jpg')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    questions_array = analyze_data()
    current_question_number = 0
    question = questions_array[current_question_number]
    player_points = 0
    running = True
    done_guess = False
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if done_guess:
                if current_question_number + 1 < len(questions_array):
                    current_question_number += 1
                    question = questions_array[current_question_number]
                    done_guess = False
                else:
                    # show result
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position (x,y) of the mouse press
                mouse_pos = event.pos
                answers_buttons = question.answers_buttons()
                for i in range(0, NUM_OF_QUESTIONS):
                    if mouse_in_button(answers_buttons[i], mouse_pos):
                        guess = question.guess(i)
                        if guess:
                            player_points += 1
                        done_guess = True

        # Update display - without input update everything
        screen.blit(background, (0, 0))
        question.display_question()
        question.display_answers()
        print(player_points)

        # display_ask_question(screen, zulu_answer, 90, (255, 0, 0))
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()
