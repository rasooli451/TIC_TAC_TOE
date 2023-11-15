import pygame

pygame.init()
def drawTable():
    for i in range(0,3):
        for j in range(0,3):
            pygame.draw.rect(screen, (30, 230, 210), [j * 200, i * 200 + 200, 200, 200])
            rect = pygame.draw.rect(screen, "black", [j * 200, i * 200 + 200, 200, 200], 5)
            RECTS[i].append(rect)
            if TABLE[i][j]==0:
                pygame.draw.circle(screen, (4, 148, 105), (rect.center), 50)
            if TABLE[i][j]==2:
                pygame.draw.line(screen ,(120, 119, 111), (rect.topleft[0] + 50, rect.topleft[1] + 50), (rect.bottomright[0] - 50, rect.bottomright[1] - 50), 10)
                pygame.draw.line(screen, (120, 119, 111), (rect.topright[0] -50, rect.topright[1] + 50), (rect.bottomleft[0] + 50, rect.bottomleft[1] - 50), 10)

def playerinput():
    global PLAYER_1
    for i in range(0,3):
        for j in range(0,3):
            if PLAYER_1:
                if RECTS[i][j].collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()==(True,False,False) and TABLE[i][j]==1:
                        TABLE[i][j] = 0
                        PLAYER_1 = False
            else:
                if RECTS[i][j].collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()==(True,False,False) and TABLE[i][j]==1:
                        TABLE[i][j] = 2
                        PLAYER_1 = True
X_SCREEN = 600
Y_SCREEN = 800
FPS = 60
PLAYER_1 = True
TABLE = [[1,1,1],
         [1,1,1],
         [1,1,1]]
RECTS =[[],[],[]]
screen = pygame.display.set_mode((X_SCREEN,Y_SCREEN))
pygame.display.set_caption("TIC-TAC-TOE")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((3, 252, 161))
    drawTable()
    playerinput()
    pygame.display.update()
    clock.tick(FPS)