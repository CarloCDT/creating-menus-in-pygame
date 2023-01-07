import pygame
import os
import sys

class Button:
    def __init__(self, txt, pos, lenght=260, width=40):
        self.text = txt
        self.pos = pos
        self.lenght = lenght
        self.width = width
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (self.lenght, self.width))

    def draw(self, screen, btn_background, btn_border, font, font_color):
        pygame.draw.rect(screen, btn_background, self.button, 0, 5)
        pygame.draw.rect(screen, btn_border, [self.pos[0], self.pos[1], self.lenght, self.width], 5, 5)
        text2 = font.render(self.text, True, font_color)
        screen.blit(text2, (self.pos[0] + self.lenght//17, self.pos[1] + self.width//5))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

# Functions
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
