import pygame as pg

grid = 24
background_color = (0, 0, 0)

pic = {}
pic['baba'] = [pg.image.load('baba_pic/baba_0_1.png'), pg.image.load('baba_pic/baba_7_1.png'), pg.image.load('baba_pic/baba_15_1.png'), pg.image.load('baba_pic/baba_23_1.png')]
pic['flag'] = [pg.image.load('baba_pic/flag_0_{}.png'.format(i)) for i in range(1,4)]
pic['wall'] = [pg.image.load('baba_pic/wall_10_1.png')]

pic['text_baba'] = [pg.image.load('baba_pic/text_baba_0_{}.png'.format(i)) for i in range(1,4)]
pic['text_is'] = [pg.image.load('baba_pic/text_is_0_{}.png'.format(i)) for i in range(1,4)]
pic['text_you'] = [pg.image.load('baba_pic/text_you_0_{}.png'.format(i)) for i in range(1,4)]
pic['text_flag'] = [pg.image.load('baba_pic/text_flag_0_{}.png'.format(i)) for i in range(1,4)]
pic['text_win'] = [pg.image.load('baba_pic/text_win_0_{}.png'.format(i)) for i in range(1,4)]
pic['text_wall'] = [pg.image.load('baba_pic/text_wall_0_{}.png'.format(i)) for i in range(1,4)]
pic['text_stop'] = [pg.image.load('baba_pic/text_stop_0_{}.png'.format(i)) for i in range(1,4)]
pic['win'] = pg.image.load('baba_pic/win.png')
