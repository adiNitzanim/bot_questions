from math import ceil

import pygame

from constants import WINDOW_WIDTH, WINDOW_HEIGHT, TEXT_FONT_SIZE, RESULTS_X, \
    RESULTS_Y, RESULTS_TEXT_COLOR, START_OVER_BUTTON_COLOR, START_OVER_X, \
    START_OVER_Y, START_OVER_WIDTH, START_OVER_HEIGHT, START_OVER_TEXT_SIZE, \
    START_OVER_TEXT_COLOR, CHAT_WINDOW_WIDTH, CHAT_WINDOW_X

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def from_text_to_array(text, text_box_width, text_font_size):
    text_array = []
    text_to_edit = text
    text_font = pygame.font.SysFont('chalkduster.ttf',
                                    text_font_size, bold=False)
    text_to_display = text_font.render(text,
                                       True, (0, 0, 0))
    text_rect = text_to_display.get_rect()
    if text_rect.width > text_box_width:
        num_of_rows = ceil(text_rect.width / text_box_width)
        line_max_length = int(len(text) / num_of_rows)
        while not (len(text_to_edit) <= 0):
            if len(text_to_edit) < line_max_length:
                text_to_edit = remove_space_from_start(text_to_edit)
                text_array.append(text_to_edit)
                text_to_edit = ""
            else:
                temp = text_to_edit[0: line_max_length]
                text_to_edit = text_to_edit[line_max_length:]
                while not (temp[-1] == ' ') and not (temp[-1] == ','):
                    text_to_edit = temp[-1] + text_to_edit
                    temp_len = int(len(temp))
                    temp = temp[0: temp_len - 1]
                temp = remove_space_from_start(temp)
                text_array.append(temp)
    else:
        text_array.append(text)
    return text_array


def remove_space_from_start(text):
    new_text = text
    if text[0] == " ":
        new_text = text[1:]
    return new_text


def center_text(rect, text_rect, row_number, num_of_rows):
    horizontal_margin = \
        (rect.height - num_of_rows * text_rect.height) // 2
    width_margin = (rect.width - text_rect.width) // 2
    text_rect.x = rect.x + width_margin
    # Center the text to the center of the post on Y axis
    text_rect.y = (rect.y + horizontal_margin +
                   row_number * text_rect.height)
    return text_rect


def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True


def display_results(player_points):
    start_over_back_rect = pygame.draw.rect(screen, START_OVER_BUTTON_COLOR,
                                            pygame.Rect(START_OVER_X,
                                                        START_OVER_Y,
                                                        START_OVER_WIDTH,
                                                        START_OVER_HEIGHT))
    results_text = pygame.font.SysFont('chalkduster.ttf',
                                       TEXT_FONT_SIZE, bold=False)
    results_display = results_text.render(
        "You have " + str(player_points) + " correct answers!",
        True, RESULTS_TEXT_COLOR)
    results_text_rect = results_display.get_rect()
    width_margin = (CHAT_WINDOW_WIDTH - results_text_rect.width) // 2
    results_text_rect.x = CHAT_WINDOW_X + width_margin
    screen.blit(results_display, (
        results_text_rect.x, RESULTS_Y))

    start_over_font = pygame.font.SysFont('chalkduster.ttf',
                                          START_OVER_TEXT_SIZE, bold=False)
    start_over_display = start_over_font.render(
        "START OVER",
        True, START_OVER_TEXT_COLOR)
    start_over_text_rect = start_over_display.get_rect()
    start_over_text_rect = center_text(start_over_back_rect,
                                       start_over_text_rect, 0, 1)
    screen.blit(start_over_display,
                (start_over_text_rect.x, start_over_text_rect.y))


def calculate_sentence_height():
    text_font = pygame.font.SysFont('chalkduster.ttf',
                                    TEXT_FONT_SIZE, bold=False)
    text_to_display = text_font.render("hello",
                                       True, (0, 0, 0))
    text_rect = text_to_display.get_rect()
    return text_rect.height
