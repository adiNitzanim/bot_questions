import pygame

from Button import Button
from Question import Question
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, QUESTION_WIDTH, \
    QUESTION_HEIGHT, QUESTION_X, QUESTION_Y, \
    START_OVER_X, START_OVER_Y, START_OVER_WIDTH, START_OVER_HEIGHT, \
    NUM_OF_ANSWERS, END_OF_CHAT_Y
from database_functions import analyze_data
from helpers import screen, mouse_in_button, display_results, roll_up


def main():

    pygame.init()
    pygame.display.set_caption('Future teller')
    clock = pygame.time.Clock()

    background = pygame.image.load('images/background.jpg')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    background_without_chat = pygame.image.load('images'
                                                '/background_without_chat.png')
    background_without_chat = pygame.transform.scale(
        background_without_chat, (WINDOW_WIDTH, WINDOW_HEIGHT))
    questions_array = analyze_data()
    current_question_number = 0
    question = questions_array[current_question_number]
    start_over_button = Button(START_OVER_X, START_OVER_Y, START_OVER_WIDTH,
                               START_OVER_HEIGHT)
    displayed_questions = [question]
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
                    prev_question = question
                    question = questions_array[current_question_number]
                    if prev_question.user_answer_y_end + question.question_answer_height > END_OF_CHAT_Y:
                        for display_question in displayed_questions:
                            display_question.set_y_pos(display_question.question_y - question.question_answer_height)
                        # roll_up(question.question_answer_height, displayed_questions)
                    question.set_y_pos(prev_question.user_answer_y_end)
                    displayed_questions.append(question)
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
            # question.display()
            for display_question in displayed_questions:
                display_question.display()
        else:
            display_results(player_points)
        screen.blit(background_without_chat, (0, 0))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


main()
