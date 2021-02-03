#!/usr/bin/env python3

import pygame
import random 
import math


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def param_generator():
    for i in range(-10, 11):
        yield i / 10


def x_dot(x, y):
    return x + y

def y_dot(x, y):
    return y


def main():
    trajectories = []

    GRIDSIZE = 6
    HALF = GRIDSIZE / 2

    for x in range(GRIDSIZE):
        for y in range(GRIDSIZE):
            x0 = (x - HALF) / HALF
            y0 = (y - HALF) / HALF
            trajectories.append(
                calculate_trajectory((x0, y0))
            )

    for x in (-0.01, 0.01):
        for y in (-0.01, 0.01):
            trajectories.append(
                calculate_trajectory((x, y))
            )

    draw(trajectories)


def calculate_trajectory(init):
    points = []
    LIMIT = 50000
    dt = 0.0001
    count_every = 50

    cur = list(init)
    for i in range(LIMIT):
        if i % count_every == 0:
            points.append(tuple(cur))
        cur[0] -= x_dot(*cur) * dt
        cur[1] -= y_dot(*cur) * dt

    points.reverse()

    cur = list(init)
    for i in range(LIMIT):
        if i % count_every == 0:
            points.append(tuple(cur))
        cur[0] += x_dot(*cur) * dt
        cur[1] += y_dot(*cur) * dt

    return points


def draw(trajectories):
    SCREEN_SIZE = (1000, 800)

    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(WHITE)

    # clock is used to set a max fps
    clock = pygame.time.Clock()


    # draw trajectories
    print("Drawing")
    scaling = SCREEN_SIZE[1] // 3
    n = 0
    for t in trajectories:
        print(f"Drawing {n+1}, has {len(t)} points")
        transformed = [
            (x[0] * scaling + SCREEN_SIZE[0] // 2, x[1] * scaling + SCREEN_SIZE[1] // 2)
            for x in t
        ]
        rand_col = [random.randint(0, 255) for i in range(3)]
        pygame.draw.lines(screen, rand_col, False, transformed)
        n += 1
        print(f"Done {n}")
    print("Done.")

    # draw axis
    pygame.draw.line(screen, BLACK, (0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2), 2)
    pygame.draw.line(screen, BLACK, (SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]), 2)

    end = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                break

        if end:
            break

        pygame.display.flip()
        clock.tick(60)



main()
