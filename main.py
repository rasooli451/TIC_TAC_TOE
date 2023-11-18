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
                pygame.draw.line(screen, (120, 119, 111), (rect.topright[0] - 50, rect.topright[1] + 50), (rect.bottomleft[0] + 50, rect.bottomleft[1] - 50), 10)
def playerinput():
    global PLAYER_1
    for i in range(0,3):
        for j in range(0,3):
            if PLAYER_1:
                if RECTS[i][j].collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()==(True,False,False) and TABLE[i][j]==1:
                        TABLE[i][j] = 0
                        Sound.play()
                        PLAYER_1 = False
            else:
                if RECTS[i][j].collidepoint(pygame.mouse.get_pos()):
                    if pygame.mouse.get_pressed()==(True,False,False) and TABLE[i][j]==1:
                        TABLE[i][j] = 2
                        Sound.play()
                        PLAYER_1 = True
def winning():
    lis=[]
    for i in range(0,3):
        lis.append(TABLE[i])
        if i==0:
           lis.append([TABLE[i][0],TABLE[i+1][0],TABLE[i+2][0]])
           lis.append([TABLE[i][0],TABLE[i+1][1],TABLE[i+2][2]])
           lis.append([TABLE[i][1], TABLE[i+1][1],TABLE[i+2][1]])
           lis.append([TABLE[i][2], TABLE[i+1][2], TABLE[i+2][2]])
           lis.append([TABLE[i][2], TABLE[i+1][1], TABLE[i+2][0]])
    for i in lis:
        if i[0]==0 and i[0]==i[1] and i[1]==i[2]:
            return True
        if i[0]==2 and i[0]==i[1] and i[1]==i[2]:
            return True
    return False
def allfilled():
    for i in range(0,3):
        for j in range(0,3):
            if TABLE[i][j]==1:
                return False
    return True
#Important variables
X_SCREEN = 600
Y_SCREEN = 800
FPS = 60
PLAYER_1 = True
Game_open = True
Game_start = True
Game_running = False
Allowed = True
TABLE = [[1,1,1],
         [1,1,1],
         [1,1,1]]
RECTS =[[],[],[]]
Sound = pygame.mixer.Sound("simple sound.wav")
#Texts
Render = pygame.font.Font(pygame.font.get_default_font(), 25)
instruct = Render.render("Press P to play, Q to quit..",False, (47, 56, 49))
instruct_rect = instruct.get_rect(center=(200,200))
Title_renderer = pygame.font.SysFont("inkfree",50, True, True)
Title = Title_renderer.render("TIC-TAC-TOE",False,(46, 70, 74))
instruct2 = Render.render("Press M to go to main menu and Q to quit.",False,(46, 70, 74))
instruct2_rect = instruct2.get_rect(center=(300, 150))
Title_rect = Title.get_rect(center=(300, 100))
#setting up the screen
screen = pygame.display.set_mode((X_SCREEN,Y_SCREEN))
pygame.display.set_caption("TIC-TAC-TOE")
BG = pygame.image.load("tic-tac-toeBG.jpg")
BG = pygame.transform.scale(BG, (X_SCREEN,Y_SCREEN)).convert_alpha()
clock = pygame.time.Clock()
while Game_open:
    if Game_start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()
               exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    Game_running = True
                if event.key==pygame.K_q:
                    Game_open = False
        screen.blit(BG, (0,0))
        screen.blit(Title,Title_rect)
        screen.blit(instruct, instruct_rect)
        pygame.display.update()
        clock.tick(FPS)
        while Game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            screen.fill((87, 167, 181))
            screen.blit(Title, Title_rect)
            drawTable()
            if Allowed:
                playerinput()
            if winning() or allfilled():
               Allowed = False
               screen.blit(instruct2,instruct2_rect)
               keys = pygame.key.get_pressed()
               if keys[pygame.K_m]:
                   Game_running = False
                   PLAYER_1 = True
                   Allowed = True
                   TABLE = [[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]]
                   RECTS = [[], [], []]
               if keys[pygame.K_q]:
                   Game_running = False
                   Game_open = False
            pygame.display.update()
            clock.tick(FPS)
