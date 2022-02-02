import pygame

from Button import Button
from constants import TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT, CHAT_WINDOW_X, \
    CHAT_WINDOW_Y, TEXT_FONT_SIZE, ANSWER_BOX_WIDTH, ANSWER_BOX_HEIGHT, \
    ANSWER_BOX_X, GAP_X, GAP_Y
from helpers import from_text_to_array, screen, center_text


class Question:

    def __init__(self, num_of_question, question_text, answers, correct_answer):
        self.text_array = from_text_to_array(question_text)
        self.answers = answers
        self.num_of_question = num_of_question
        self.correct_answer = correct_answer

        # fields for display_question
        text_font = pygame.font.SysFont('chalkduster.ttf',
                                        TEXT_FONT_SIZE, bold=False)
        text_to_display = text_font.render(self.text_array[0],
                                           True, (0, 0, 0))
        text_rect = text_to_display.get_rect()
        self.sentence_height = text_rect.height
        self.question_height = text_rect.height * len(self.text_array)
        self.chat_y = CHAT_WINDOW_Y
        self.guess_number = -1


    # display the question text and possible answers
    def display_question(self):
        text_font = pygame.font.SysFont('chalkduster.ttf',
                                        TEXT_FONT_SIZE, bold=False)
        text_to_display = text_font.render(self.text_array[0],
                                           True, (0, 0, 0))
        text_rect = text_to_display.get_rect()
        text_height = text_rect.height
        pygame.draw.rect(screen, (255, 255, 255),
                         pygame.Rect(CHAT_WINDOW_X,
                                     self.chat_y,
                                     TEXT_BOX_WIDTH,
                                     self.question_height + 10))
        for i in range(0, len(self.text_array)):
            text_font = pygame.font.SysFont('chalkduster.ttf',
                                            TEXT_FONT_SIZE, bold=False)
            text_to_display = text_font.render(self.text_array[i],
                                               True, (0, 0, 0))
            screen.blit(text_to_display, (
            CHAT_WINDOW_X + 5, CHAT_WINDOW_Y + 5 + (text_height * i)))

    def display_answers(self):
        first_answer_y = self.chat_y + self.question_height + GAP_Y
        for i in range(0, len(self.answers)):
            color = (255, 255, 255)
            if self.guess_number > -1 and self.guess_number == i:
                if self.guess_number == self.correct_answer:
                    color = (0, 255, 0)
                else:
                    color = (255, 0, 0)

            text_font = pygame.font.SysFont('chalkduster.ttf',
                                            TEXT_FONT_SIZE, bold=False)
            text_to_display = text_font.render(self.answers[i],
                                               True, (0, 0, 0))
            text_rect = text_to_display.get_rect()
            rect = pygame.draw.rect(screen, color,
                                    pygame.Rect(ANSWER_BOX_X + ((i % 2) * (
                                                ANSWER_BOX_WIDTH + GAP_X)),
                                                first_answer_y + ((i // 2) * (
                                                            ANSWER_BOX_HEIGHT + (
                                                                GAP_Y // 2))),
                                                ANSWER_BOX_WIDTH,
                                                ANSWER_BOX_HEIGHT))
            text_rect = center_text(rect, text_rect)
            screen.blit(text_to_display, (text_rect.x, text_rect.y))

    def answers_buttons(self):
        answers_buttons = []
        for i in range(0, len(self.answers)):
            answers_buttons.append(
                Button(ANSWER_BOX_X + ((i % 2) * (
                                                ANSWER_BOX_WIDTH + GAP_X)),
                                                self.chat_y + self.question_height + GAP_Y + ((i // 2) * (
                                                            ANSWER_BOX_HEIGHT + (
                                                                GAP_Y // 2))),
                                                ANSWER_BOX_WIDTH,
                                                ANSWER_BOX_HEIGHT))
        return answers_buttons

    def guess(self, num_of_answer):
        self.guess_number = num_of_answer
        if self.correct_answer == num_of_answer:
            return True
        else:
            return False


