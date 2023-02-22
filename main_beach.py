import pygame
import pygame as pg
import sys
import os
import random
from pygame.locals import *
import time
from dobrynia import Hodit
from res_count import res_count
from load_image_loc import load_image
from Boardd import Board

pygame.init()
flags = FULLSCREEN | DOUBLEBUF
WIDTH = 1280
HEIGHT = 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc = screen
lstx = []
index = 0
lsty = []
m = 0
with open('a.txt') as fp2:
    lines = fp2.readlines()

all_sprites = pygame.sprite.Group()
border1 = pygame.sprite.Group()
border2 = pygame.sprite.Group()
border3 = pygame.sprite.Group()
border4 = pygame.sprite.Group()
border5 = pygame.sprite.Group()
border6 = pygame.sprite.Group()
tree_sprites = pygame.sprite.Group()
dobrinya = pygame.sprite.Group()
b = pygame.sprite.Group()


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, name):
        super().__init__(b)
        if x1 == x2:
            self.add(name)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(name)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


board = Board(40, 21)
clock = pygame.time.Clock()
a = Hodit(dobrinya)

running = True
board.random_spawn_trees(50,  lstx, lsty, tree_sprites, 'clay_test2.png', 30, 12)
Border(1, 1, WIDTH - 1, 1, border1)
Border(9, 90, 9, HEIGHT - 3, border2)
Border(3, HEIGHT - 200, WIDTH - 390, HEIGHT - 200, border3)
Border(WIDTH - 9, 3, WIDTH - 9, HEIGHT - 3, border4)
Border(WIDTH - 260, HEIGHT - 200, WIDTH - 9, HEIGHT - 3, border3)
Border(212, 90, WIDTH - 1, 1, border1)
Border(212, 60, WIDTH - 1, 30, border3)
Border(202, 60, 202, 85, border4)
Border(WIDTH - 270, HEIGHT - 200, WIDTH - 270, HEIGHT - 40, border4)
Border(WIDTH - 380, HEIGHT - 200, WIDTH - 380, HEIGHT - 40, border2)
Border(WIDTH - 380, HEIGHT - 40, WIDTH - 270, HEIGHT - 40, border3)
Border(9, 90, 110, 90, border1)
Border(9, 60, 110, 60, border3)
Border(120, 60, 120, 85, border2)
pg.display.flip()
flag1 = False
flag2 = False
flag3 = False
flag4 = False
spin = False
shiz = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            pass
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                if a.update2(border2):
                    flag1 = True
                    index = 7

            if event.key == pygame.K_s:
                if a.update3(border3):
                    flag2 = True
                    index = 4

            if event.key == pygame.K_w:
                if a.update1(border1):
                    flag3 = True
                    index = 1

            if event.key == pygame.K_d:
                if a.update4(border4):
                    flag4 = True
                    index = 10

            if event.key == pygame.K_e:
                if a.update5(border4):
                    spin = True
                    index = 0

            if event.key == pygame.K_q:
                if a.update6(border4):
                    shiz = True
                    index = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                flag1 = False
            if event.key == pygame.K_s:
                flag2 = False
            if event.key == pygame.K_w:
                flag3 = False
            if event.key == pygame.K_d:
                flag4 = False
            if event.key == pygame.K_e:
                spin = False
            if event.key == pygame.K_q:
                shiz = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.f += 1
            board.rubit(dobrinya, lstx, lsty, tree_sprites, lines, event.pos, 1)
            with open('a.txt', 'r') as f:
                l = f.readlines()
            res_count(screen, l)

    if spin:
        if a.update5(border4):
            a.image = a.images[index]
            dis = pg.image.load('data\\dislike.png')
            dis_rect = dis.get_rect(bottomright=((a.rect.x + 80), (a.rect.y + 15)))
            sc.blit(dis, dis_rect)
            pg.display.update()
            index += 1
            if index >= 12:
                index = 0
    if shiz:
        if a.update6(border4):
            a.image = a.images[index]
            imgs = ["data\\m1.png", "data\\m2.png", "data\\m3.png", "data\\m4.png"]
            m += 1
            dis = pg.image.load(imgs[m])
            dis_rect = dis.get_rect(bottomright=((a.rect.x + 40), (a.rect.y + 15)))
            sc.blit(dis, dis_rect)
            pg.display.update()
            index += 1
            if index >= 12:
                index = 0
            if m >= 3:
                m = 0

    if flag1:
        if a.update2(border2):
            a.rect.x -= 11
        a.image = a.images[index]
        index += 1
        if index >= 9:
            index = 7
    if flag2:
        if a.update3(border3):
            a.rect.y += 11
        a.image = a.images[index]
        index += 1
        if index >= 6:
            index = 4
    if flag3:
        if a.update1(border1):
            a.rect.y -= 11

        a.image = a.images[index]
        index += 1
        if index >= 3:
            index = 1

    if flag4:
        if a.update4(border4):
            a.rect.x += 11
        a.image = a.images[index]
        index += 1
        if index >= 12:
            index = 10
    board.rerender(screen, 'test_beach1.png')
    all_sprites.draw(screen)
    tree_sprites.draw(screen)
    dobrinya.draw(screen)
    res_count(screen, lines)
    if a.rect.x <= 80 and a.rect.y <= 40:
        os.system('start main.py')
        sys.exit()
    else:
        clock.tick(30)
        pg.display.update()
