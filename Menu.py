import pygame
from Button import Button
from Chess import play
pygame.init()


# Feito por Miguel Almeida Morais no dia 1 de Junho de 2023.


scrn = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Tic Tac Toe Chess")

BS = pygame.image.load("images/TicTacToe.png")


def get_font(size):
    return pygame.font.Font("images/Lasting Sketch.ttf", size)


def main_menu():
    while True:
        scrn.blit(BS, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 50))

        PLAY_BUTTON = Button(image=pygame.image.load("images/Play_button.png"), pos=(300, 300), text_pos=(300, 295), text_input="PLAY", font=get_font(65), base_color="White", hovering_color="#d7fcd4")

        QUIT_BUTTON = Button(image=pygame.image.load("images/Quit_Button.png"), pos=(300, 500), text_pos=(300, 495), text_input="QUIT", font=get_font(65), base_color="White", hovering_color="#d7fcd4")

        scrn.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(scrn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()

        pygame.display.update()


main_menu()
