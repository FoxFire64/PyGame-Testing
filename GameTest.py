import pygame


def init(disp_w, disp_h):
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

    game_exit = False

    # Event handler loop
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting Game...")
                game_exit = True

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


        x += x_change
        y += y_change
        window.fill(white)
        car(x, y)

        # collision check point
        if collision_check(x, y): game_exit = True

        pygame.display.update()  # or use .flip(), like a flipbook
        clock.tick(60)
    print("Thanks for playing!")


def collision_check(x, y):

    if x < 0:
        window.fill(white)
        car(0, y)
        pygame.display.update()
        return True
    elif x > disp_w - car_w:
        window.fill(white)
        car((disp_w - car_w), y)
        pygame.display.update()
        return True

    if y < 0:
        window.fill(white)
        car(x, 0)
        pygame.display.update()
        return True
    elif y > disp_h - car_h:
        window.fill(white)
        car(x, (disp_h - car_h))
        pygame.display.update()
        return True


if __name__ == '__main__':

    disp_w, disp_h = 800, 600
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    window, title, clock = init(disp_w, disp_h)

    car_img = pygame.image.load('Car-100h.png')
    car_w, car_h = 54, 100

    run()
    pygame.quit()
    quit()
