import pygame as pg
import config
import maps
import Movement4 as Movement

def tuple_mul(a,b):
    return (int(a[0] * b), int(a[1] * b))
def update(screen, shot):
    
    screen.fill(config.background_color)
    for i in shot.objects:
        for pos in shot.objects[i]:
            screen.blit(config.pic[i][0], tuple_mul(pos, config.grid))
    for i in shot.dir_objects:
        for pos in shot.dir_objects[i]:
            screen.blit(config.pic[i][0], tuple_mul(pos, config.grid))
    pg.display.flip()


def main():
    pg.init()
    screen = pg.display.set_mode((maps.test.width * config.grid, maps.test.height * config.grid))
    pg.display.set_caption('baba is you')
    update(screen, maps.test)

    run = True
    shot = maps.test
    while run:
        for event in pg.event.get():
            #print(event)
            if event.type == pg.QUIT:
                run = False
            elif shot.win == False and event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    shot = Movement.up(shot)
                elif event.key == pg.K_DOWN:
                    shot = Movement.down(shot)
                elif event.key == pg.K_LEFT:
                    shot = Movement.left(shot)
                elif event.key == pg.K_RIGHT:
                    shot = Movement.right(shot)
            if shot.win:
                screen.fill(config.background_color)
                screen.blit(config.pic['win'], tuple_mul(tuple_mul((shot.width, shot.height), config.grid), 0.5))
                pg.display.flip()
            else:
                update(screen, shot)

    pg.quit()

if __name__ == "__main__":
    main()
