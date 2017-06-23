import random

import pygame
import time


def init():
    pygame.init()
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    return pygame.display.set_mode((disp_w, disp_h)), \
           pygame.display.set_caption('Racin\' Stripes'), \
           pygame.time.Clock()


def car(x, y):
    window.blit(car_img, (x, y))


def run():
    x = (disp_w * 0.45)
    y = (disp_h * 0.8)
    x_change, y_change = 0, 0
    car_change_amt = 5

    ob_w, ob_h = 60, 80
    ob_start_x = random.randrange(0, disp_w - ob_w)
    ob_start_y = -600
    ob_speed = 7

    y_list = range(disp_h, 0, (ob_h + 5) * -2)
    road_coord = (disp_w / 2) - (ob_w / 2)

    game_exit = False
    starting_msg_display()
    # Event handler loop
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting Game...")
                print("Thanks for playing!")
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -car_change_amt
                elif event.key == pygame.K_RIGHT:
                    x_change = car_change_amt
                elif event.key == pygame.K_UP:
                    y_change = -car_change_amt
                elif event.key == pygame.K_DOWN:
                    y_change = car_change_amt

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x, y = x + x_change, y + y_change
        window.fill(white)

        y_list = [y_coord + ob_speed for y_coord in y_list]

        for y_coord in y_list:
            # create the object at each coordinate in center of screen
            draw_obj(road_coord, y_coord, ob_w, ob_h, black)

        y_list = [0 - ob_h if y_coord > disp_h else y_coord for y_coord in y_list]

        car(x, y)

        # collision check point
        if crash(x, y): game_exit = True

        pygame.display.update()  # or use .flip(), like a flipbook
        clock.tick(60)
    print("Thanks for playing!")


def draw_road():
    return None  # TODO : create something here


def draw_obj(coord_x, ob_y, ob_w, ob_h, color):
    pygame.draw.rect(window, color, [coord_x, ob_y, ob_w, ob_h])


def txt_objects(txt, font):
    txt_surface = font.render(txt, True, black)
    return txt_surface, txt_surface.get_rect()


def starting_msg_display():
    msg_display("Starting Game in...", 80)
    msg_display("3..", 80)
    msg_display("2..", 80)
    msg_display("1..", 80)


def msg_display(txt, size):
    window.fill(white)
    formatting = pygame.font.Font('freesansbold.ttf', size)

    txt_surface, txt_cont = txt_objects(txt, formatting)
    txt_cont.center = ((disp_w / 2), (disp_h / 2))
    window.blit(txt_surface, txt_cont)
    pygame.display.update()
    time.sleep(1)


def restart():
    time.sleep(2)

    run()


def crash(x, y):
    if x < 0:
        window.fill(white)
        car(0, y)
        pygame.display.update()
        msg_display("You crashed", 80)
        restart()
        return True
    elif x > disp_w - car_w:
        window.fill(white)
        car((disp_w - car_w), y)
        pygame.display.update()
        msg_display("You crashed", 80)
        restart()
        return True

    if y < 0:
        window.fill(white)
        car(x, 0)
        pygame.display.update()
        msg_display("You crashed", 80)
        restart()
        return True
    elif y > disp_h - car_h:
        window.fill(white)
        car(x, (disp_h - car_h))
        pygame.display.update()
        msg_display("You crashed", 80)
        restart()
        return True


if __name__ == '__main__':
    disp_w, disp_h = 800, 600
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    window, title, clock = init()

    car_img = pygame.image.load('Car-100h.png')
    car_w, car_h = 54, 100

    run()
    pygame.quit()
    quit()
