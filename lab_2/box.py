import pygame
import random
import time

# Initialize pygame
pygame.init()

# Define constants
WIDTH = 600
HEIGHT = 600
GRID_SIZE = 3
TILE_SIZE = WIDTH // GRID_SIZE
EMPTY_TILE = 0
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
TILE_COLOR = (200, 200, 200)
TEXT_COLOR = (0, 0, 0)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-Puzzle")

# Fonts for text
font = pygame.font.SysFont("arial", 40)

# Function to draw the grid
def draw_grid(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            tile = board[row][col]
            pygame.draw.rect(screen, TILE_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
            if tile != EMPTY_TILE:
                text = font.render(str(tile), True, TEXT_COLOR)
                screen.blit(text, (x + TILE_SIZE // 3, y + TILE_SIZE // 3))

    # Draw the grid lines
    for x in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (x * TILE_SIZE, 0), (x * TILE_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, LINE_COLOR, (0, x * TILE_SIZE), (WIDTH, x * TILE_SIZE), 2)

# Function to check if puzzle is solved
def is_solved(board):
    target = list(range(1, GRID_SIZE * GRID_SIZE)) + [EMPTY_TILE]
    flat_board = [tile for row in board for tile in row]
    return flat_board == target

# Function to move the tile
def move_tile(board, empty_pos, direction):
    x, y = empty_pos
    if direction == "up" and y > 0:
        board[y][x], board[y - 1][x] = board[y - 1][x], board[y][x]
        return (x, y - 1)
    elif direction == "down" and y < GRID_SIZE - 1:
        board[y][x], board[y + 1][x] = board[y + 1][x], board[y][x]
        return (x, y + 1)
    elif direction == "left" and x > 0:
        board[y][x], board[y][x - 1] = board[y][x - 1], board[y][x]
        return (x - 1, y)
    elif direction == "right" and x < GRID_SIZE - 1:
        board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]
        return (x + 1, y)
    return empty_pos

# Function to generate a random puzzle board
def generate_board():
    numbers = list(range(GRID_SIZE * GRID_SIZE))
    random.shuffle(numbers)
    board = [numbers[i:i + GRID_SIZE] for i in range(0, len(numbers), GRID_SIZE)]
    return board

# Main game loop
def main():
    board = generate_board()
    empty_pos = (board.index([EMPTY_TILE]) % GRID_SIZE, board.index([EMPTY_TILE]) // GRID_SIZE)
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_grid(board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    empty_pos = move_tile(board, empty_pos, "up")
                elif event.key == pygame.K_DOWN:
                    empty_pos = move_tile(board, empty_pos, "down")
                elif event.key == pygame.K_LEFT:
                    empty_pos = move_tile(board, empty_pos, "left")
                elif event.key == pygame.K_RIGHT:
                    empty_pos = move_tile(board, empty_pos, "right")
        
        # Check if puzzle is solved
        if is_solved(board):
            print("Puzzle Solved!")
            running = False

        pygame.display.update()
        pygame.time.Clock().tick(30)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
