import pygame
from game_utils import Button, resource_path

pygame.init()

WIDTH = 1280
HEIGHT = 800
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
icon_url = resource_path('img/icon.png')
img = pygame.display.set_icon(pygame.image.load(icon_url)) # Icon
pygame.display.set_caption('Ultimate Tic-Tac-Toe')
main_menu = False
font = pygame.font.SysFont('system', 24)
title_font = pygame.font.SysFont('system', 48)
logo_url = resource_path('img/logo.png')
logo = pygame.transform.scale(pygame.image.load(logo_url), (1000, 340))
menu_command = 0

# Colors
background_color = (9,102,130)
btn_background = (205, 230, 245)
btn_border = (25, 25, 25)
font_color = (25, 25, 25)

def draw_menu():
    command = -1

    # Render Title
    txt = title_font.render('Main Manu', True, 'black')
    screen.blit(txt, (100, 100))

    # Game Modes
    button1 = Button('Game Mode: 1', (120, 180), 500, 40)
    button1.draw(screen, btn_background, btn_border, font, font_color)
    button2 = Button('Game Mode: 2', (120, 240), 500, 40)
    button2.draw(screen, btn_background, btn_border, font, font_color)
    button3 = Button('Game Mode: 3', (120, 300), 500, 40)
    button3.draw(screen, btn_background, btn_border, font, font_color)

    exit_menu = Button('Back', (120, 400))
    exit_menu.draw(screen, btn_background, btn_border, font, font_color)

    if exit_menu.check_clicked():
        command = 0
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    return command

def draw_game():
    menu_btn = Button('Play', (WIDTH-300, HEIGHT-75))
    menu_btn.draw(screen, btn_background, btn_border, font, font_color)
    menu = menu_btn.check_clicked()
    screen.blit(logo, (140, 200))
    return menu

run = True
while run:
    screen.fill(background_color)
    timer.tick(fps)

    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False
    else:
        main_menu = draw_game()
        if menu_command > 0:
            text = font.render(f'Game Mode: {menu_command} pressed!', True, 'black')
            screen.blit(text, (150, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
