import pygame

from Button import Button
from constants import QUESTION_X, \
    QUESTION_Y, QUESTION_FONT_SIZE, ANSWER_BOX_WIDTH, ANSWER_BOX_HEIGHT, \
    ANSWER_BOX_X, GAP_X, GAP_Y, QUESTION_WIDTH, QUESTION_HEIGHT, \
    ANSWER_FONT_SIZE, USER_ANSWER_X
from helpers import from_text_to_array, screen, center_text, \
    calculate_sentence_height


class Question:

    def __init__(self, num_of_question, question_text, answers, correct_answer):
        self.text_array = from_text_to_array(question_text, QUESTION_WIDTH,
                                             QUESTION_FONT_SIZE)
        self.answers = answers
        for i in range(0, len(self.answers)):
            answers[i] = from_text_to_array(answers[i], ANSWER_BOX_WIDTH,
                                            ANSWER_FONT_SIZE)
        self.num_of_question = num_of_question
        self.correct_answer = correct_answer
        self.question_height = calculate_sentence_height() * len(
            self.text_array)
        self.guess_answer_number = -1
        self.question_y = QUESTION_Y
        self.question_y_end = self.question_y + self.question_height + (
                    1.5 * GAP_Y) + 2 * ANSWER_BOX_HEIGHT
        self.user_answer_y_end = self.question_y_end + 2*(GAP_Y//2) + (calculate_sentence_height()*len(self.answers[self.guess_answer_number]))
        self.question_answer_height = self.user_answer_y_end - self.question_y

    def display(self):
        self.display_question()
        self.display_answers()
        self.display_user_answer()

    def display_question(self):
        text_font = pygame.font.SysFont('chalkduster.ttf',
                                        QUESTION_FONT_SIZE, bold=False)
        text_to_display = text_font.render(self.text_array[0],
                                           True, (0, 0, 0))
        text_rect = text_to_display.get_rect()
        text_height = text_rect.height
        pygame.draw.rect(screen, (255, 255, 255),
                         pygame.Rect(QUESTION_X,
                                     self.question_y,
                                     QUESTION_WIDTH,
                                     self.question_height + 10))
        for i in range(0, len(self.text_array)):
            text_font = pygame.font.SysFont('chalkduster.ttf',
                                            QUESTION_FONT_SIZE, bold=False)
            text_to_display = text_font.render(self.text_array[i],
                                               True, (0, 0, 0))
            screen.blit(text_to_display, (
                QUESTION_X + 5, self.question_y + 5 + (text_height * i)))

    def display_answers(self):
        first_answer_y = self.question_y + self.question_height + GAP_Y
        for i in range(0, len(self.answers)):
            color = (255, 255, 255)
            if self.guess_answer_number > -1 and self.guess_answer_number == i:
                if self.guess_answer_number == self.correct_answer:
                    color = (0, 255, 0)
                else:
                    color = (255, 0, 0)
            rect = pygame.draw.rect(screen, color,
                                    pygame.Rect(ANSWER_BOX_X + ((i % 2) * (
                                            ANSWER_BOX_WIDTH + GAP_X)),
                                                first_answer_y + ((i // 2) * (
                                                        ANSWER_BOX_HEIGHT + (
                                                        GAP_Y // 2))),
                                                ANSWER_BOX_WIDTH,
                                                ANSWER_BOX_HEIGHT))
            for j in range(0, len(self.answers[i])):
                text_font = pygame.font.SysFont('chalkduster.ttf',
                                                QUESTION_FONT_SIZE, bold=False)
                text_to_display = text_font.render(self.answers[i][j],
                                                   True, (0, 0, 0))
                text_rect = text_to_display.get_rect()

                text_rect = center_text(rect, text_rect, j,
                                        len(self.answers[i]))
                screen.blit(text_to_display, (text_rect.x, text_rect.y))

    def display_user_answer(self):
        if not self.guess_answer_number == -1:
            rect = pygame.draw.rect(screen, (255, 255, 255),
                                    pygame.Rect(USER_ANSWER_X,
                                                self.question_y_end
                                                + (GAP_Y // 2),
                                                ANSWER_BOX_WIDTH,
                                                calculate_sentence_height() * len(
                                                    self.answers[self.guess_answer_number])))
            for i in range(0, len(self.answers[self.guess_answer_number])):
                text_font = pygame.font.SysFont('chalkduster.ttf',
                                                QUESTION_FONT_SIZE, bold=False)
                text_to_display = text_font.render(
                    self.answers[self.guess_answer_number][i],
                    True, (0, 0, 0))
                text_rect = text_to_display.get_rect()

                text_rect = center_text(rect, text_rect, i,
                                        len(self.answers[i]))
                screen.blit(text_to_display, (text_rect.x, text_rect.y))

    def answers_buttons(self):
        answers_buttons = []
        for i in range(0, len(self.answers)):
            answers_buttons.append(
                Button(ANSWER_BOX_X + ((i % 2) * (
                        ANSWER_BOX_WIDTH + GAP_X)),
                       self.question_y + self.question_height + GAP_Y + (
                               (i // 2) * (
                               ANSWER_BOX_HEIGHT + (
                               GAP_Y // 2))),
                       ANSWER_BOX_WIDTH,
                       ANSWER_BOX_HEIGHT))
        return answers_buttons

    def guess(self, num_of_answer):
        self.guess_answer_number = num_of_answer
        if self.correct_answer == num_of_answer:
            return True
        else:
            return False

    def restart(self):
        self.guess_answer_number = -1

    def set_y_pos(self, y_pos):
        self.question_y = y_pos
        self.question_y_end = self.question_y + self.question_height + (
                1.5 * GAP_Y) + 2 * ANSWER_BOX_HEIGHT
        self.user_answer_y_end = self.question_y_end + 2 * (GAP_Y // 2) + (
                    calculate_sentence_height() * len(
                self.answers[self.guess_answer_number]))
        self.question_answer_height = self.user_answer_y_end - self.question_y
