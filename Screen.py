import pygame
import random
import Soldier
import consts
import Mine

screen = pygame.display.set_mode((1000, 500))
randoms_list = []



def set_caption():
    pygame.display.set_caption("Flag Game")


def create_random_index():
    for num in range(20):
        current_width = random.randint(10, 950)
        current_height = random.randint(10, 450)
        randoms_list.append((current_width, current_height))


def basic_background():
    screen.fill(consts.SCREEN_COLOR)
    grass_img = pygame.image.load('grass.png')
    grass_img = pygame.transform.scale(grass_img, (50, 35))

    image = grass_img.copy()
    for num in range(20):
        screen.blit(image, randoms_list[num])
    show_soldier()
    show_flag()
    pygame.display.flip()


def grid_background(mines_list):
    screen.fill((128, 0, 0))
    WIDTH = 18.99
    HEIGHT = 18.99
    MARGIN = 1
    for row in range(consts.GAME_GRID_ROWS):
        for col in range(consts.GAME_GRID_COLS):
            pygame.draw.rect(screen,
                             (0, 0, 0),
                             [(MARGIN + WIDTH) * col + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    show_night_soldier()
    show_mines(mines_list)
    pygame.display.flip()


def show_soldier():
    soldier_img = pygame.image.load('soldier.png')
    soldier_img = pygame.transform.scale(soldier_img, (37.98, 75.96))
    index = Soldier.updated_body_area[0]
    image = soldier_img
    screen.blit(image, (index[1]*20, index[0]*20))


def show_night_soldier():
    soldier_img = pygame.image.load('night_soldier.png')
    soldier_img = pygame.transform.scale(soldier_img, (37.98, 75.96))
    index = Soldier.updated_body_area[0]
    image = soldier_img
    screen.blit(image, (index[1]*20, index[0]*20))



def show_flag():
    flag_img = pygame.image.load('flag.png')
    flag_img = pygame.transform.scale(flag_img, (75.96, 56.97))
    image = flag_img
    screen.blit(image, (consts.FLAG_STARTING_POINT[1]*20, consts.FLAG_STARTING_POINT[0]*20))


def show_mines(mines_list):
    mine_image = pygame.image.load('mine.png')
    mine_image = pygame.transform.scale(mine_image, (56.97, 18.99))
    image = mine_image
    for mine in range(0, len(mines_list), 3):
        index = mines_list[mine]
        print(index)

        screen.blit(image, (index[1]*20, index[0]*20))




