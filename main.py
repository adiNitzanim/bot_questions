import pygame

from Button import Button
from Question import Question
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, CHAT_WINDOW_WIDTH, \
    CHAT_WINDOW_HEIGHT, CHAT_WINDOW_X, CHAT_WINDOW_Y,  \
    START_OVER_X, START_OVER_Y, START_OVER_WIDTH, START_OVER_HEIGHT, \
    NUM_OF_ANSWERS
from database_functions import analyze_data
from helpers import screen, mouse_in_button, display_results


def main():

    pygame.init()
    pygame.display.set_caption('Future teller')
    clock = pygame.time.Clock()

    background = pygame.image.load('images/background.jpg')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    questions_array = analyze_data()
    current_question_number = 0
    question = questions_array[current_question_number]
    start_over_button = Button(START_OVER_X, START_OVER_Y, START_OVER_WIDTH,
                               START_OVER_HEIGHT)
    player_points = 0
    running = True
    finish_questions = False
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
                    finish_questions = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position (x,y) of the mouse press
                mouse_pos = event.pos
                answers_buttons = question.answers_buttons()
                for i in range(0, NUM_OF_ANSWERS):
                    if mouse_in_button(answers_buttons[i], mouse_pos):
                        guess = question.guess(i)
                        if guess:
                            player_points += 1
                        done_guess = True
                if finish_questions and mouse_in_button(start_over_button,
                                                        mouse_pos):
                    current_question_number = 0
                    player_points = 0
                    finish_questions = False
                    done_guess = False
                    for quest in questions_array:
                        quest.restart()
                    question = questions_array[current_question_number]

        screen.blit(background, (0, 0))
        if not finish_questions:
            question.display()
        else:
            display_results(player_points)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


main()
