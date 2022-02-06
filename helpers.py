from math import ceil

import pygame

from constants import WINDOW_WIDTH, WINDOW_HEIGHT, TEXT_FONT_SIZE

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
        print(text, text_rect.width, text_box_width, num_of_rows, len(text), line_max_length, len(text) / num_of_rows)
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
    print(text_array)
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
