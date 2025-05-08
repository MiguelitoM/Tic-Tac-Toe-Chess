import pygame
import Centrar
import Movements
import Button
from Button import Button


# Feito por Miguel Almeida Morais no dia 1 de Junho de 2023.


pygame.init()
X = 600
Y = 700
White = (255, 255, 255)
Fundo = (48, 44, 44)
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Tic Tac Toe Chess')
FPS = 60
piecessize = (100, 100)
boardsize = (300, 300)
boardposition = (150, 200)
piecesposition = [(150, 550), (250, 550), (350, 550), (150, 50), (250, 50), (350, 50)]
movecavalo = False
movebispo = False
movetorre = False
setupcavalob = True
setupbispob = True
setuptorreb = True
setupcavalop = True
setupbispop = True
setuptorrep = True
confirmarmeio = False
turn = 0
win = -1

board = (pygame.image.load("images/Board.png"))
CB = (pygame.image.load("images/CB.svg"))
BB = (pygame.image.load("images/BB.svg"))
TB = (pygame.image.load("images/TB.svg"))
CP = (pygame.image.load("images/CP.svg"))
BP = (pygame.image.load("images/BP.svg"))
TP = (pygame.image.load("images/TP.svg"))

board = pygame.transform.scale(board, boardsize)
CB = pygame.transform.scale(CB, piecessize)
BB = pygame.transform.scale(BB, piecessize)
TB = pygame.transform.scale(TB, piecessize)
CP = pygame.transform.scale(CP, piecessize)
BP = pygame.transform.scale(BP, piecessize)
TP = pygame.transform.scale(TP, piecessize)


def draw_window(cavalob, bispob, torreb, cavalop, bispop, torrep, turn):
    scrn.fill(White)
    scrn.blit(board, boardposition)
    scrn.blit(CB, (cavalob.x, cavalob.y))
    scrn.blit(BB, (bispob.x, bispob.y))
    scrn.blit(TB, (torreb.x, torreb.y))
    scrn.blit(CP, (cavalop.x, cavalop.y))
    scrn.blit(BP, (bispop.x, bispop.y))
    scrn.blit(TP, (torrep.x, torrep.y))
    if turn == 0:
        turntext = "Turn: White"
    else:
        turntext = "Turn: Black"
    turn_text = get_font(30).render(turntext, True, "Black")
    turn_rect = turn_text.get_rect(center=(60, 30))
    scrn.blit(turn_text, turn_rect)
    pygame.display.update()


def checkpiece(x, y, cavalob, bispob, torreb, cavalop, bispop, torrep):
    if x <= 150 or x >= 450 or y <= 200 or y >= 500:
        return True
    else:
        if cavalob.collidepoint(x, y) or cavalop.collidepoint(x, y) or bispob.collidepoint(x, y) or bispop.collidepoint(x, y) or torreb.collidepoint(x, y) or torrep.collidepoint(x, y):
            return True
        else:
            return False


def whiteblocked(cavalob, bispob, torreb, cavalop, bispop, torrep):
    global win
    # Brancas
    if checkpiece((bispob.centerx + 100), (bispob.centery + 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((bispob.centerx - 100), (bispob.centery + 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((bispob.centerx + 100), (bispob.centery - 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((bispob.centerx - 100), (bispob.centery - 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and not setupbispob:
        bispobblocked = True
    else:
        bispobblocked = False

    if checkpiece((torreb.centerx + 100), (torreb.centery + 0), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((torreb.centerx + 0), (torreb.centery + 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((torreb.centerx - 100), (torreb.centery + 0), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((torreb.centerx + 0), (torreb.centery - 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and not setuptorreb:
        torrebblocked = True
    else:
        torrebblocked = False
    if checkpiece((cavalob.centerx + 200), (cavalob.centery + 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalob.centerx + 200), (cavalob.centery - 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalob.centerx - 200), (cavalob.centery + 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalob.centerx - 200), (cavalob.centery - 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalob.centerx + 100), (cavalob.centery + 200), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalob.centerx + 100), (cavalob.centery - 200), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalob.centerx - 100), (cavalob.centery + 200), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalob.centerx - 100), (cavalob.centery - 200), cavalob, bispob, torreb, cavalop, bispop, torrep) and not setupcavalob:
        cavalobblocked = True
    else:
        cavalobblocked = False
    if cavalobblocked and bispobblocked and torrebblocked and turn == 0:
        win = 1

# Pretas
    if checkpiece((bispop.centerx + 100), (bispop.centery + 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((bispop.centerx - 100), (bispop.centery + 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((bispop.centerx + 100), (bispop.centery - 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((bispop.centerx - 100), (bispop.centery - 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and not setupbispop:
        bispopblocked = True
    else:
        bispopblocked = False

    if checkpiece((torrep.centerx + 100), (torrep.centery + 0), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((torrep.centerx + 0), (torrep.centery + 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((torrep.centerx - 100), (torrep.centery + 0), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((torrep.centerx + 0), (torrep.centery - 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and not setuptorrep:
        torrepblocked = True
    else:
        torrepblocked = False
    if checkpiece((cavalop.centerx + 200), (cavalop.centery + 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalop.centerx + 200), (cavalop.centery - 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalop.centerx - 200), (cavalop.centery + 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalop.centerx - 200), (cavalop.centery - 100), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalop.centerx + 100), (cavalop.centery + 200), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalop.centerx + 100), (cavalop.centery - 200), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalop.centerx - 100), (cavalop.centery + 200), cavalob, bispob, torreb, cavalop, bispop, torrep) and checkpiece((cavalop.centerx - 100), (cavalop.centery - 200), cavalob, bispob, torreb, cavalop, bispop, torrep) and not setupcavalop:
        cavalopblocked = True
    else:
        cavalopblocked = False
    if cavalopblocked and bispopblocked and torrepblocked and turn == 1:
        win = 0


def get_font(size):
    return pygame.font.Font("images/Lasting Sketch.ttf", size)


def gameresult(cavalob, bispob, torreb, cavalop, bispop, torrep):
    global win
    # Diagonal
    if abs(cavalob.x - bispob.x) == abs(cavalob.y - bispob.y) == 200 and (torreb.x, torreb.y) == (250, 300):
        win = 0
    if abs(cavalob.x - torreb.x) == abs(cavalob.y - torreb.y) == 200 and (bispob.x, bispob.y) == (250, 300):
        win = 0
    if abs(bispob.x - torreb.x) == abs(bispob.y - torreb.y) == 200 and (torreb.x, torreb.y) == (250, 300):
        win = 0

    if abs(cavalop.x - bispop.x) == abs(cavalop.y - bispop.y) == 200 and (torrep.x, torrep.y) == (250, 300):
        win = 1
    if abs(cavalop.x - torrep.x) == abs(cavalop.y - torrep.y) == 200 and (bispop.x, bispop.y) == (250, 300):
        win = 1
    if abs(bispop.x - torrep.x) == abs(bispop.y - torrep.y) == 200 and (torrep.x, torrep.y) == (250, 300):
        win = 1

    # Horizontal
    if cavalob.y == bispob.y == torreb.y and not (setupcavalob or setupbispob or setuptorreb):
        win = 0
    if cavalop.y == bispop.y == torrep.y and not (setupcavalop or setupbispop or setuptorrep):
        win = 1

    # Vertical
    if cavalob.x == bispob.x == torreb.x and not (setupcavalob or setupbispob or setuptorreb):
        win = 0
    if cavalop.x == bispop.x == torrep.x and not (setupcavalop or setupbispop or setuptorrep):
        win = 1


def endgame(winner):
    while True:
        scrn.fill(White)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        WIN_TEXT = get_font(100).render(f'{winner} wins!', True, "Black")   # #b68f40
        MENU_RECT = WIN_TEXT.get_rect(center=(300, 50))

        PLAY_BUTTON = Button(image=pygame.image.load("images/Play_button.png"), pos=(300, 300), text_pos=(300, 295), text_input="PLAY AGAIN", font=get_font(65), base_color="White", hovering_color="#d7fcd4")

        QUIT_BUTTON = Button(image=pygame.image.load("images/Quit_Button.png"), pos=(300, 500), text_pos=(300, 495), text_input="QUIT", font=get_font(65), base_color="White", hovering_color="#d7fcd4")

        scrn.blit(WIN_TEXT, MENU_RECT)

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


def play():
    global movecavalo, movebispo, movetorre, event, turn, setupcavalob, setupcavalop, setupbispob, setupbispop, setuptorreb, setuptorrep, confirmarmeio, win
    cavalob = pygame.Rect(piecesposition[0], piecessize)
    bispob = pygame.Rect(piecesposition[1], piecessize)
    torreb = pygame.Rect(piecesposition[2], piecessize)
    cavalop = pygame.Rect(piecesposition[3], piecessize)
    bispop = pygame.Rect(piecesposition[4], piecessize)
    torrep = pygame.Rect(piecesposition[5], piecessize)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Se fecho a janela, o jogo acaba.
            draw_window(cavalob, bispob, torreb, cavalop, bispop, torrep, turn)
            whiteblocked(cavalob, bispob, torreb, cavalop, bispop, torrep)
            gameresult(cavalob, bispob, torreb, cavalop, bispop, torrep)
            if win >= 0:
                pygame.time.wait(500)
                if win == 0:
                    winner = "White"
                else:
                    winner = "Black"
                win = -1
                turn = 0
                setupcavalob = True
                setupbispob = True
                setuptorreb = True
                setupcavalop = True
                setupbispop = True
                setuptorrep = True
                endgame(winner)


# Movimentos

# CavaloBranco
            if event.type == pygame.MOUSEBUTTONDOWN and cavalob.collidepoint(pygame.mouse.get_pos()) and turn == 0:
                movecavalo = True
                movetorre = False
                movebispo = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and movecavalo and turn == 0 and not cavalob.collidepoint(pygame.mouse.get_pos()) and not cavalop.collidepoint(pygame.mouse.get_pos()) and not bispob.collidepoint(pygame.mouse.get_pos()) and not bispob.collidepoint(pygame.mouse.get_pos()) and not torreb.collidepoint(pygame.mouse.get_pos()) and not torrep.collidepoint(pygame.mouse.get_pos()):
                    movecavalo = False
                    mouse = pygame.mouse.get_pos()
                    mouse = Centrar.centrar(mouse[0], mouse[1])
                    if mouse is not None:
                        if setupcavalob:
                            (cavalob.x, cavalob.y) = (mouse[0] - 50, mouse[1] - 50)
                            setupcavalob = False
                            turn = 1
                        if Movements.movcavalo(abs(mouse[0]-(cavalob.x+50)), abs(mouse[1]-(cavalob.y+50))) and not setupcavalob and not setupbispob and not setuptorreb:
                            (cavalob.x, cavalob.y) = (mouse[0] - 50, mouse[1] - 50)
                            turn = 1


# CavaloPreto
            if event.type == pygame.MOUSEBUTTONDOWN and cavalop.collidepoint(pygame.mouse.get_pos()) and turn == 1:
                movecavalo = True
                movetorre = False
                movebispo = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and movecavalo and turn == 1 and not cavalob.collidepoint(pygame.mouse.get_pos()) and not cavalop.collidepoint(pygame.mouse.get_pos()) and not bispob.collidepoint(pygame.mouse.get_pos()) and not bispob.collidepoint(pygame.mouse.get_pos()) and not torreb.collidepoint(pygame.mouse.get_pos()) and not torrep.collidepoint(pygame.mouse.get_pos()):
                    mouse = pygame.mouse.get_pos()
                    mouse = Centrar.centrar(mouse[0], mouse[1])
                    movecavalo = False
                    if mouse is not None:
                        if setupcavalop:
                            (cavalop.x, cavalop.y) = (mouse[0] - 50, mouse[1] - 50)
                            setupcavalop = False
                            turn = 0
                        if Movements.movcavalo(abs(mouse[0]-(cavalop.x+50)), abs(mouse[1]-(cavalop.y+50))) and not setupcavalop and not setupbispop and not setuptorrep:
                            (cavalop.x, cavalop.y) = (mouse[0] - 50, mouse[1] - 50)
                            turn = 0

# BispoBranco
            if event.type == pygame.MOUSEBUTTONDOWN and bispob.collidepoint(pygame.mouse.get_pos()) and turn == 0:
                movecavalo = False
                movebispo = True
                movetorre = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and movebispo and turn == 0 and not cavalob.collidepoint(pygame.mouse.get_pos()) and not cavalop.collidepoint(pygame.mouse.get_pos()) and not bispob.collidepoint(pygame.mouse.get_pos()) and not bispob.collidepoint(pygame.mouse.get_pos()) and not torreb.collidepoint(pygame.mouse.get_pos()) and not torrep.collidepoint(pygame.mouse.get_pos()):
                    mouse = pygame.mouse.get_pos()
                    mouse = Centrar.centrar(mouse[0], mouse[1])
                    movebispo = False
                    if mouse is not None:
                        if setupbispob:
                            (bispob.x, bispob.y) = (mouse[0] - 50, mouse[1] - 50)
                            setupbispob = False
                            turn = 1
                        if Movements.movbispo(mouse[0]-(bispob.x+50), mouse[1]-(bispob.y+50)) and not setupcavalob and not setupbispob and not setuptorreb:
                            if abs(mouse[0]-(bispob.x+50)) == 200:
                                if not checkpiece((mouse[0]+bispob.x+50)/2, (mouse[1]+bispob.y+50)/2, cavalob, bispob, torreb, cavalop, bispop, torrep):
                                    (bispob.x, bispob.y) = (mouse[0] - 50, mouse[1] - 50)
                                    turn = 1
                            else:
                                (bispob.x, bispob.y) = (mouse[0] - 50, mouse[1] - 50)
                                turn = 1

# BispoPreto
            if event.type == pygame.MOUSEBUTTONDOWN and bispop.collidepoint(pygame.mouse.get_pos()) and turn == 1:
                movecavalo = False
                movebispo = True
                movetorre = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and movebispo and turn == 1 and not cavalob.collidepoint(pygame.mouse.get_pos()) and not cavalop.collidepoint(pygame.mouse.get_pos()) and not bispob.collidepoint(pygame.mouse.get_pos()) and not bispob.collidepoint(pygame.mouse.get_pos()) and not torreb.collidepoint(pygame.mouse.get_pos()) and not torrep.collidepoint(pygame.mouse.get_pos()):
                    mouse = pygame.mouse.get_pos()
                    mouse = Centrar.centrar(mouse[0], mouse[1])
                    movebispo = False
                    if mouse is not None:
                        if setupbispop:
                            (bispop.x, bispop.y) = (mouse[0] - 50, mouse[1] - 50)
                            setupbispop = False
                            turn = 0
                        if Movements.movbispo(mouse[0]-(bispop.x+50), mouse[1]-(bispop.y+50)) and not setupcavalop and not setupbispop and not setuptorrep:
                            if abs(mouse[0]-(bispop.x+50)) == 200:
                                if not checkpiece((mouse[0]+bispop.x+50)/2, (mouse[1]+bispop.y+50)/2, cavalob, bispob, torreb, cavalop, bispop, torrep):
                                    (bispop.x, bispop.y) = (mouse[0] - 50, mouse[1] - 50)
                                    turn = 0
                            else:
                                (bispop.x, bispop.y) = (mouse[0] - 50, mouse[1] - 50)
                                turn = 0

# TorreBranca
            if event.type == pygame.MOUSEBUTTONDOWN and torreb.collidepoint(pygame.mouse.get_pos()) and turn == 0:
                movecavalo = False
                movebispo = False
                movetorre = True
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and movetorre and turn == 0 and not cavalob.collidepoint(pygame.mouse.get_pos()) and not cavalop.collidepoint(pygame.mouse.get_pos()) and not bispob.collidepoint(pygame.mouse.get_pos()) and not bispop.collidepoint(pygame.mouse.get_pos()) and not torreb.collidepoint(pygame.mouse.get_pos()) and not torrep.collidepoint(pygame.mouse.get_pos()):
                    mouse = pygame.mouse.get_pos()
                    mouse = Centrar.centrar(mouse[0], mouse[1])
                    movetorre = False
                    if mouse is not None:
                        if setuptorreb:
                            (torreb.x, torreb.y) = (mouse[0] - 50, mouse[1] - 50)
                            setuptorreb = False
                            turn = 1
                        if Movements.movtorre(mouse[0]-(torreb.x+50), mouse[1]-(torreb.y+50)) and not setupcavalob and not setupbispob and not setuptorreb:
                            if abs(mouse[0]-(torreb.x+50)) == 200 or abs(mouse[1]-(torreb.y+50)) == 200:
                                if not checkpiece((mouse[0]+torreb.x+50)/2, (mouse[1]+torreb.y+50)/2, cavalob, bispob, torreb, cavalop, bispop, torrep):
                                    (torreb.x, torreb.y) = (mouse[0] - 50, mouse[1] - 50)
                                    turn = 1
                            else:
                                (torreb.x, torreb.y) = (mouse[0] - 50, mouse[1] - 50)
                                turn = 1

# TorrePreta
            if event.type == pygame.MOUSEBUTTONDOWN and torrep.collidepoint(pygame.mouse.get_pos()) and turn == 1:
                movecavalo = False
                movebispo = False
                movetorre = True
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and movetorre and turn == 1 and not checkpiece(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], cavalob, bispob, torreb, cavalop, bispop, torrep):
                    mouse = pygame.mouse.get_pos()
                    mouse = Centrar.centrar(mouse[0], mouse[1])
                    movetorre = False
                    if mouse is not None:
                        if setuptorrep:
                            (torrep.x, torrep.y) = (mouse[0] - 50, mouse[1] - 50)
                            setuptorrep = False
                            turn = 0
                        if Movements.movtorre(mouse[0]-(torrep.x+50), mouse[1]-(torrep.y+50)) and not setupcavalop and not setupbispop and not setuptorrep:
                            if abs(mouse[0]-torrep.centerx) == 200 or abs(mouse[1]-torrep.centery) == 200:
                                if not checkpiece((mouse[0]+torrep.x+50)/2, (mouse[1]+torrep.y+50)/2, cavalob, bispob, torreb, cavalop, bispop, torrep):
                                    (torrep.x, torrep.y) = (mouse[0] - 50, mouse[1] - 50)
                                    turn = 0
                            else:
                                (torrep.x, torrep.y) = (mouse[0] - 50, mouse[1] - 50)
                                turn = 0
