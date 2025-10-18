import pygame,time
#Biến
width = height = 712
o = 1
x = 1
matrix = [0,
          0,0,0,
          0,0,0,
          0,0,0]
player = 'p1'
text1 = 'PLAY AGAIN'
play = True
delay = 1
xwin = ['x1','x2','x3']
owin = ['o1','o2','o3']
#Pygame load
pygame.init()
screen = pygame.display.set_mode((width,height))
fps = pygame.time.Clock()
board = pygame.image.load('assets/textures/board.png')
x_texture = pygame.image.load('assets/textures/x.png')
o_texture = pygame.image.load('assets/textures/o.png')
p1win = pygame.image.load('assets/textures/p1win.png')
p2win = pygame.image.load('assets/textures/p2win.png')
playagain = pygame.image.load('assets/textures/playagain.png')
p1win_rect = p1win.get_rect(center = (356,356))
p2win_rect = p2win.get_rect(center = (356,356))
playagain_rect = playagain.get_rect(center = (356,435))
game_font = pygame.font.Font('assets/Nevanta-Black.otf',35)
move_font = pygame.font.Font('assets/Nevanta-Black.otf',50)
#Rect nhận diện (mỗi ô cách 169 pixels)
empty_rect1 = o_texture.get_rect(center = (187,187)) #1/1
empty_rect2 = o_texture.get_rect(center = (356,187)) #1/2
empty_rect3 = o_texture.get_rect(center = (524,187)) #1/3
empty_rect4 = o_texture.get_rect(center = (187,356)) #2/1
empty_rect5 = o_texture.get_rect(center = (356,356)) #2/2
empty_rect6 = o_texture.get_rect(center = (524,356)) #2/3
empty_rect7 = o_texture.get_rect(center = (187,524)) #3/1
empty_rect8 = o_texture.get_rect(center = (356,524)) #3/2
empty_rect9 = o_texture.get_rect(center = (524,524)) #3/3
#Hàm
def click(player,matrix,o,x,t):
    if player == 'p2':
        if f'o{o}' in matrix:
            d = matrix.index(f'o{o}')
            matrix[d] = 0
        matrix[t] = f'o{o}'
        if o == 3:
            o = 1
        else:
            o += 1
        player = 'p1'
    elif player == 'p1':
        if f'x{x}' in matrix:
            d = matrix.index(f'x{x}')
            matrix[d] = 0
        matrix[t] = f'x{x}'
        if x == 3:
            x = 1
        else:
            x += 1
        player = 'p2'
    return player,matrix,o,x
# ======= LÀM TỐI MÀN HÌNH =========
def dark():
    dark_overlay = pygame.Surface((712, 712))   # tạo surface mới
    dark_overlay.set_alpha(150)                 # độ trong suốt (0-255, càng cao càng tối)
    dark_overlay.fill((0, 0, 0))                # tô màu đen
    screen.blit(dark_overlay, (0, 0))
# ======= Play again ========= 
def pa(color,matrix,delay):
    dark()
    play = False
    if player_win == 'x':
        screen.blit(p1win,p1win_rect)
    elif player_win == 'o':
        screen.blit(p2win,p2win_rect)
    if (356-118) <= mouse_x <= (356+118) and (435-35) <= mouse_y <= (435+35):
        color = 'light gray'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                play = True
                matrix = [0,0,0,0,0,0,0,0,0,0]
                delay = 1
    else:
        color = 'white'
    pygame.draw.rect(screen, color, playagain_rect, border_radius=10)
    playagain_text = game_font.render(text1,True, (0,0,0))
    playagain_text_rect = playagain_text.get_rect(center = (356,435))
    screen.blit(playagain_text,playagain_text_rect)

    return play,matrix,delay
    
#While loop
run = True
while run:
    #Thoát Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
    #Vị trí chuột
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #Nền
    screen.fill('light gray')
    screen.blit(board,(100,100))
    #Bộ nhận diện
    if play == True:
        if (187-77.5) <= mouse_x <= (187+77.5) and (187-77.5) <= mouse_y <= (187+77.5): #O/X 1
            pygame.draw.rect(screen, 'gray',empty_rect1)
            if event.type == pygame.MOUSEBUTTONDOWN and matrix[1] == 0:
                if event.button == 1:
                    player, matrix, o, x = click(player,matrix,o,x,1)
        if (356-77.5) <= mouse_x <= (356+77.5) and (187-77.5) <= mouse_y <= (187+77.5): #O/X 2
            pygame.draw.rect(screen, 'gray',empty_rect2)
            if event.type == pygame.MOUSEBUTTONDOWN and matrix[2] == 0:
                if event.button == 1:
                    player, matrix, o, x = click(player,matrix,o,x,2)
        if (524-77.5) <= mouse_x <= (524+77.5) and (187-77.5) <= mouse_y <= (187+77.5): #O/X 3
            pygame.draw.rect(screen, 'gray',empty_rect3)
            if event.type == pygame.MOUSEBUTTONDOWN and matrix[3] == 0:
                if event.button == 1:
                    player, matrix, o, x = click(player,matrix,o,x,3)
        if (187-77.5) <= mouse_x <= (187+77.5) and (356-77.5) <= mouse_y <= (356+77.5): #O/X 4
            pygame.draw.rect(screen, 'gray',empty_rect4)
            if event.type == pygame.MOUSEBUTTONDOWN and matrix[4] == 0:
                if event.button == 1:
                    player, matrix, o, x = click(player,matrix,o,x,4)
        if (356-77.5) <= mouse_x <= (356+77.5) and (367-77.5) <= mouse_y <= (356+77.5): #O/X 5
            pygame.draw.rect(screen, 'gray',empty_rect5)
            if event.type == pygame.MOUSEBUTTONDOWN and matrix[5] == 0:
                if event.button == 1:
                    player, matrix, o, x = click(player,matrix,o,x,5)
        if (524-77.5) <= mouse_x <= (524+77.5) and (356-77.5) <= mouse_y <= (356+77.5): #O/X 6
            pygame.draw.rect(screen, 'gray',empty_rect6)
            if event.type == pygame.MOUSEBUTTONDOWN and matrix[6] == 0:
                if event.button == 1:
                    player, matrix, o, x = click(player,matrix,o,x,6)
        if (187-77.5) <= mouse_x <= (187+77.5) and (524-77.5) <= mouse_y <= (524+77.5): #O/X 7
            pygame.draw.rect(screen, 'gray',empty_rect7)
            if event.type == pygame.MOUSEBUTTONDOWN and matrix[7] == 0:
                if event.button == 1:
                    player, matrix, o, x = click(player,matrix,o,x,7)
        if (356-77.5) <= mouse_x <= (356+77.5) and (524-77.5) <= mouse_y <= (524+77.5): #O/X 8
            pygame.draw.rect(screen, 'gray',empty_rect8)
            if event.type == pygame.MOUSEBUTTONDOWN and matrix[8] == 0:
                if event.button == 1:
                    player, matrix, o, x = click(player,matrix,o,x,8)
        if (524-77.5) <= mouse_x <= (524+77.5) and (524-77.5) <= mouse_y <= (524+77.5): #O/X 9
            pygame.draw.rect(screen, 'gray',empty_rect9)
            if event.type == pygame.MOUSEBUTTONDOWN and matrix[9] == 0:
                if event.button == 1:
                    player, matrix, o, x = click(player,matrix,o,x,9)
#In O/X
    #O/x 1
    if matrix[1] == 'o1' or matrix[1] == 'o2' or matrix[1] == 'o3':
        screen.blit(o_texture,empty_rect1)
    elif matrix[1] == 'x1' or matrix[1] == 'x2' or matrix[1] == 'x3':
        screen.blit(x_texture,empty_rect1)
    #o/x 2
    if matrix[2] == 'o1' or matrix[2] == 'o2' or matrix[2] == 'o3':
        screen.blit(o_texture,empty_rect2)
    elif matrix[2] == 'x1' or matrix[2] == 'x2' or matrix[2] == 'x3':
        screen.blit(x_texture,empty_rect2)
    #o/x 3
    if matrix[3] == 'o1' or matrix[3] == 'o2' or matrix[3] == 'o3':
        screen.blit(o_texture,empty_rect3)
    elif matrix[3] == 'x1' or matrix[3] == 'x2' or matrix[3] == 'x3':
        screen.blit(x_texture,empty_rect3)
    #o/x 4
    if matrix[4] == 'o1' or matrix[4] == 'o2' or matrix[4] == 'o3':
        screen.blit(o_texture,empty_rect4)
    elif matrix[4] == 'x1' or matrix[4] == 'x2' or matrix[4] == 'x3':
        screen.blit(x_texture,empty_rect4)
    #o/x 5
    if matrix[5] == 'o1' or matrix[5] == 'o2' or matrix[5] == 'o3':
        screen.blit(o_texture,empty_rect5)
    elif matrix[5] == 'x1' or matrix[5] == 'x2' or matrix[5] == 'x3':
        screen.blit(x_texture,empty_rect5)
    #o/x 6
    if matrix[6] == 'o1' or matrix[6] == 'o2' or matrix[6] == 'o3':
        screen.blit(o_texture,empty_rect6)
    elif matrix[6] == 'x1' or matrix[6] == 'x2' or matrix[6] == 'x3':
        screen.blit(x_texture,empty_rect6)
    #o/x 7
    if matrix[7] == 'o1' or matrix[7] == 'o2' or matrix[7] == 'o3':
        screen.blit(o_texture,empty_rect7)
    elif matrix[7] == 'x1' or matrix[7] == 'x2' or matrix[7] == 'x3':
        screen.blit(x_texture,empty_rect7)
    #o/x 8
    if matrix[8] == 'o1' or matrix[8] == 'o2' or matrix[8] == 'o3':
        screen.blit(o_texture,empty_rect8)
    elif matrix[8] == 'x1' or matrix[8] == 'x2' or matrix[8] == 'x3':
        screen.blit(x_texture,empty_rect8)
    #o/x 9
    if matrix[9] == 'o1' or matrix[9] == 'o2' or matrix[9] == 'o3':
        screen.blit(o_texture,empty_rect9)
    elif matrix[9] == 'x1' or matrix[9] == 'x2' or matrix[9] == 'x3':
        screen.blit(x_texture,empty_rect9)
#In lượt người chơi
    if player == 'p1':
        xmove = move_font.render("X to move", True, 'red')
        xmovet_rect = xmove.get_rect(center = (356,70))
        screen.blit(xmove,xmovet_rect)
    if player == 'p2':
        omove = move_font.render("O to move", True, 'blue')
        omovet_rect = omove.get_rect(center = (356,70))
        screen.blit(omove,omovet_rect)
#Kiểm tra người thắng
    #Check hàng ngang
    if sorted(map(str, matrix[1:4])) == xwin or sorted(map(str, matrix[4:7])) == xwin or sorted(map(str, matrix[7:])) == xwin:
        delay = 0
        play = False
        player_win = 'x'
        play,matrix,delay = pa('White',matrix,delay)
        if delay == 1:
            time.sleep(0.5)
            delay = 0
    if sorted(map(str, matrix[1:4])) == owin or sorted(map(str, matrix[4:7])) == owin or sorted(map(str, matrix[7:])) == owin:
        delay = 0
        play = False
        player_win = 'o'
        play,matrix,delay = pa('White',matrix,delay)
        if delay == 1:
            time.sleep(0.5)
            delay = 0
    #Check hàng dọc
    if sorted(map(str, [matrix[1],matrix[4],matrix[7]])) == xwin or sorted(map(str, [matrix[2],matrix[5],matrix[8]])) == xwin or sorted(map(str, [matrix[3],matrix[6],matrix[9]])) == xwin:
        delay = 0
        play = False
        player_win = 'x'
        play,matrix,delay = pa('White',matrix,delay)
        if delay == 1:
            time.sleep(0.5)
            delay = 0
    if sorted(map(str, [matrix[1],matrix[4],matrix[7]])) == owin or sorted(map(str, [matrix[2],matrix[5],matrix[8]])) == owin or sorted(map(str, [matrix[3],matrix[6],matrix[9]])) == owin:
        delay = 0
        play = False
        player_win = 'o'
        play,matrix,delay = pa('White',matrix,delay)
        if delay == 1:
            time.sleep(0.5)
            delay = 0
    #Check đường chéo
    if sorted(map(str, [matrix[1],matrix[5],matrix[9]])) == xwin or sorted(map(str, [matrix[3],matrix[5],matrix[7]])) == xwin:
        delay = 0
        play = False
        player_win = 'x'
        play,matrix,delay = pa('White',matrix,delay)
        if delay == 1:
            time.sleep(0.5)
            delay = 0
    if sorted(map(str, [matrix[1],matrix[5],matrix[9]])) == owin or sorted(map(str, [matrix[3],matrix[5],matrix[7]])) == owin:
        delay = 0
        play = False
        player_win = 'o'
        play,matrix,delay = pa('White',matrix,delay)
        if delay == 1:
            time.sleep(0.5)
            delay = 0

    pygame.display.update()
    fps.tick(60)