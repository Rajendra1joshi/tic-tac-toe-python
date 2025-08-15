import pygame
import sys

pygame.init()

HEIGHT = 300
WIDTH = 300
LINE_COLOR = (50,50,50)
LINE_WIDTH = 5
font = pygame.font.Font(None, 72)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

def create_board():
    return [["" for _ in range(3)] for _ in range(3)]

def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
        
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                return board[0][col]
        
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        
        if board[2][0] == board[1][1] == board[0][2] != "":
            return board[2][0]
        
        for row in board:
            for cell in row:
                if cell == "":
                    return None
                
        return "Tie"
    
board = create_board()
player = "X"
winner = None

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = create_board()
                player = "X"
                winner = None

        if event.type == pygame.MOUSEBUTTONUP and winner is None:
            x,y = pygame.mouse.get_pos()

            col = x // 100
            row = y // 100

            if board[row][col] == "":
                board[row][col] = player

                player = "O" if player == "X" else "X"

                winner = check_winner(board)

        screen.fill((240, 240, 240))

        #Draw the lines grid

        pygame.draw.line(screen,LINE_COLOR,(100, 0),(100, HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(200, 0 ),(200, HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(0, 100),(WIDTH, 100),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR,(0, 200),(WIDTH, 200),LINE_WIDTH)

        for row in range(3):
            for col in range(3):

                mark = board[row][col]

                if mark != "":
                    text_surface = font.render(mark, True, (220, 20, 60))
                    x_pos = col * 100 + 50 - text_surface.get_width() // 2
                    y_pos = row * 100 + 50 - text_surface.get_height() // 2
                    screen.blit(text_surface,(x_pos,y_pos))

        if winner is not None:
            if winner == "Tie":
                msg = "It's Tie!"
            else:
                msg = f"{winner} Wins!"

                end_font = pygame.font.Font(None, 50)
                text_surface = end_font.render(msg, True,(10,15,20))
                screen.blit(text_surface,(WIDTH // 2 - text_surface.get_width()//2, HEIGHT // 2 - text_surface.get_height() // 2))

        pygame.display.update()

pygame.quit()
sys.exit()
