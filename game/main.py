import pygame
import numpy as np


WIDTH = 1000
ROWS = 30
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Electric Field Emulator")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
    """Node rect class."""

    def __init__(self, row, col, width, total_rows):
        """defines node's attributes."""
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.total_rows = total_rows
        self.padding = WIDTH // ROWS // 10

        # physics properties
        self.q = 0
        self.charged = False
        self.arrow = ((self.x + self.padding, self.y + 0.3 * self.width),
                      (self.x + self.width * 0.5, self.y + 0.3 * self.width),
                      (self.x + self.width * 0.5, self.y + self.padding),
                      (self.x + self.width - self.padding, self.y + 0.5 * self.width),
                      (self.x + self.width * 0.5, self.y + self.width - self.padding),
                      (self.x + self.width * 0.5, self.y + 0.7 * self.width),
                      (self.x + self.padding, self.y + 0.7 * self.width))

    def get_pos(self):
        """get the grid's position of a node."""
        return self.row, self.col

    def is_charged(self):
        """checks if node is closed - meaning it's already been checked."""
        return self.charged

    def reset(self):
        """reset node's color & "role" in the grid"""
        self.charged = False
        self.q = 0

    def make_charge(self):
        """makes the node color black - barrier."""
        self.charged = True
        self.q = 1

    def draw(self, win):
        """draws each node according to its coordinates."""
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

        if self.is_charged():
            pygame.draw.circle(win, RED, (self.x + self.width // 2, self.y + self.width // 2),
                               self.width // 2 - self.padding)
        else:
            pygame.draw.polygon(win, (0, 0, 0), self.arrow)

    def __repr__(self):
        return f"Spot[{self.x = }, {self.y = }, {self.width = }, {self.arrow = }]"


def make_grid(rows, width):
    """makes grid system with nodes."""
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(win, rows, width):
    """draws grid lines."""
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    """basic screen settings & updates."""
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    """gets the node the user clicked on from x,y values."""
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def E(q, coordinates: list, x, y):
    r_3 = np.hypot(x - coordinates[0], y - coordinates[1]) ** 3
    return q * (x - coordinates[0]) / r_3, q * (y - coordinates[1]) / r_3


def main():
    grid = make_grid(ROWS, WIDTH)

    start = None
    end = None

    run = True
    while run:
        draw(WIN, grid, ROWS, WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                spot = grid[row][col]
                spot.make_charge()
                pass

            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                spot = grid[row][col]
                spot.reset()
                pass

            if event.type == pygame.KEYDOWN:
                pass

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)

    pygame.quit()


if __name__ == '__main__':
    main()
