'''game'''
import pygame
import sys
import os

pygame.init()

scr_width = 1000
scr_height = 475

win = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption('Game')

bg = pygame.image.load('bg.png')

clock = pygame.time.Clock()


runRight = [pygame.image.load('run_right/run_0.png'), pygame.image.load('run_right/run_1.png'), pygame.image.load('run_right/run_2.png'),
            pygame.image.load('run_right/run_3.png'), pygame.image.load('run_right/run_4.png'), pygame.image.load('run_right/run_5.png')]
runLeft = [pygame.image.load('run_left/run-left-00.png'), pygame.image.load('run_left/run-left-01.png'), pygame.image.load('run_left/run-left-02.png'),
           pygame.image.load('run_left/run-left-03.png'), pygame.image.load('run_left/run-left-04.png'), pygame.image.load('run_left/run-left-05.png')]
stand = pygame.image.load('player_movement/idle/idle_0.png')
jump = [pygame.image.load('player_movement/jump/jump_0.png'), pygame.image.load('player_movement/jump/jump_1.png'),
        pygame.image.load('player_movement/jump/jump_2.png'), pygame.image.load('player_movement/jump/jump_3.png')]
sword_attack1 = [pygame.image.load('player_combat/sword_fighting/attack_1/attack1_0.png'), pygame.image.load('player_combat/sword_fighting/attack_1/attack1_1.png'), pygame.image.load(
    'player_combat/sword_fighting/attack_1/attack1_2.png'), pygame.image.load('player_combat/sword_fighting/attack_1/attack1_3.png'),
    pygame.image.load('player_combat/sword_fighting/attack_1/attack1_4.png')]
punch = [pygame.image.load('player_combat/punch/punch/punch_0.png'), pygame.image.load('player_combat/punch/punch/punch_1.png'), pygame.image.load('player_combat/punch/punch/punch_2.png'),
         pygame.image.load('player_combat/punch/punch/punch_3.png'),
         pygame.image.load('player_combat/punch/punch/punch_4.png'), pygame.image.load('player_combat/punch/punch/punch_5.png'), pygame.image.load(
    'player_combat/punch/punch/punch_6.png'), pygame.image.load('player_combat/punch/punch/punch_7.png'), pygame.image.load('player_combat/punch/punch/punch_8.png'),
    pygame.image.load('player_combat/punch/punch/punch_9.png'), pygame.image.load(
        'player_combat/punch/punch/punch_10.png'), pygame.image.load('player_combat/punch/punch/punch_11.png'),
    pygame.image.load('player_combat/punch/punch/punch_12.png')]
runPunch = [pygame.image.load('player_combat/punch/run_punch/run_punch_0.png'), pygame.image.load('player_combat/punch/run_punch/run_punch_1.png'), pygame.image.load('player_combat/punch/run_punch/run_punch_2.png'), pygame.image.load(
    'player_combat/punch/run_punch/run_punch_3.png'), pygame.image.load('player_combat/punch/run_punch/run_punch_4.png'), pygame.image.load('player_combat/punch/run_punch/run_punch_5.png'), pygame.image.load('player_combat/punch/run_punch/run_punch_6.png')]


class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

        # left, right, stand
        self.moveLeft = False
        self.moveRight = False
        self.standing = True
        self.walkCount = 0

        self.left = False
        self.right = False

        # jumping
        self.isJump = False
        self.jumpCount = 10

        # attacking
        self.swordAttackCount = 0
        self.swordAttack = False

        self.punchAttack = False
        self.punchCount = 0

        self.runPunchAttack = False
        self.runPunchCount = 0

    def walk(self, win):
        if self.walkCount >= 30:
            self.walkCount = 0

        if not(self.standing):
            if self.moveLeft:
                win.blit(runLeft[self.walkCount // 6], (self.x, self.y))
                self.walkCount += 1
                self.x -= self.vel
            elif self.moveRight:
                win.blit(runRight[self.walkCount // 6], (self.x, self.y))
                self.walkCount += 1
                self.x += self.vel
        else:
            win.blit(stand, (self.x, self.y))

    def jump(self, win):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (fighter.jumpCount ** 2) * .5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.standing = True
                self.jumpCount = 10
            win.blit(jump[self.jumpCount // 8], (self.x, self.y))

    def melee(self, win):

        if self.swordAttackCount >= 10:
            self.swordAttackCount = 0

        if self.swordAttack:
            win.blit(
                sword_attack1[self.swordAttackCount // 2], (self.x, self.y))
            self.standing = False
            self.swordAttackCount += 1

    def punch(self, win):
        if self.punchCount >= 26:
            self.punchCount = 0

        if self.punchAttack:
            win.blit(punch[self.punchCount // 2], (self.x, self.y))
            self.standing = False
            self.punchCount += 1

    def runPunch(self, win):
        if self.runPunchCount >= 14:
            self.runPunchCount = 0

        if self.right:
            if self.runPunchAttack:
                win.blit(runPunch[self.runPunchCount // 2], (self.x, self.y))
                self.standing = False
                self.x += self.vel
                self.runPunchCount += 1
            if self.left:
                if self.runPunchAttack:
                    win.blit(runPunch[self.runPunchCount // 2],
                             (self.x, self.y))
                    self.standing = False
                    self.runPunchCount += 1


def redrawGameWindow():
    win.blit(bg, (0, 0))
    fighter.walk(win)
    fighter.jump(win)
    fighter.melee(win)
    fighter.punch(win)
    fighter.runPunch(win)
    pygame.display.update()


fighter = player(200, 380, 64, 64)


while True:

    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                fighter.moveRight = True
                fighter.moveLeft = False
                fighter.standing = False
            if event.key == pygame.K_LEFT:
                fighter.moveLeft = True
                fighter.moveRight = False
                fighter.standing = False
            if event.key == pygame.K_SPACE:
                fighter.isJump = True
                fighter.standing = False
                fighter.moveLeft = False
                fighter.moveRight = False
            if event.key == pygame.K_x:
                fighter.swordAttack = True
                fighter.moveRight = False
                fighter.moveLeft = False
            if event.key == pygame.K_c:
                fighter.punchAttack = True
                fighter.moveRight = False
                fighter.moveLeft = False
            # if event.key == pygame.K_z:
            #     fighter.runPunchAttack = True
            #     fighter.right = False
            #     fighter.left = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                fighter.standing = True
            if event.key == pygame.K_LEFT:
                fighter.standing = True
            if event.key == pygame.K_x:
                fighter.swordAttack = False
                fighter.standing = True
            if event.key == pygame.K_c:
                fighter.punchAttack = False
                fighter.standing = True
            if event.key == pygame.K_z:
                fighter.runPunchAttack = False
                fighter.standing = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and keys[pygame.K_z]:
            fighter.runPunchAttack = True
            fighter.moveRight = False
            fighter.right = True
            fighter.moveLeft = False
            fighter.standing = False

        if keys[pygame.K_LEFT]:
            fighter.moveLeft = True
            fighter.moveRight = False
            fighter.standing = False
        if keys[pygame.K_SPACE]:
            fighter.isJump = True
            fighter.standing = False
            fighter.moveLeft = False
            fighter.moveRight = False

    redrawGameWindow()
