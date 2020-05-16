import pygame



def main():
    pygame.init()
    snake_speed_clock = pygame.time.clock()
    screen = pygame.display.set_mode((windows_width, windows_height))
    screen.fill(white)

    pygame.display.set_caption("python 贪吃蛇")
    show_start_info(screen)
    while True:
        running_game(screen, snake_speed_clock)
        show_gameover_info(screen)

def show_start_info(screen):
    font = pygame.font.Font('myfont.ttf', 40)
    tip = font.render("按任意键开始游戏", True, (65, 105, 225))


def running_game(screen, snake_speed, speed_clock):
    pass

def draw_food(screen):
    pass

def draw_snake():
    pass

def draw_grid():
    pass
