# Разработал ст-т гр. ИУ7-25: Руднев К.

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (149, 158, 149)
VIOLET = (89, 89, 161)
# Инициализация используемых цветов

pygame.init()
# Инициализация модуля

size = (700, 500)
screen = pygame.display.set_mode(size)
# Установка размеров и создание сцены

pygame.display.set_caption("The Best EVER Horror")
# Создание заголовка

done = False

clock = pygame.time.Clock()
# Инициализация таймера

speed_man_x = 2.7
speed_stone_x = 2.799
# Скорость объектов вдоль оси x

speed_man_y = -1.5
speed_stone_y = 8
speed_speare = 2.5
speed_peaks = 2.5
# Скорость объектов вдоль оси y

start_hand1_x = 15
start_hand2_x = 37
start_head_x = 15
start_leg1_x = 10
start_leg2_x = 46
start_puzo_x = 15

end_hand1_x = 0
end_hand2_x = 52
end_leg1_x = 18
end_leg2_x = 35
# Начальные координаты объектов человечка по оси x

start_stone_x = 5
start_peak11_x = 360
start_peak21_x = 376
start_peak31_x = 368

start_peak12_x = 378
start_peak22_x = 394
start_peak32_x = 386

start_peak13_x = 396
start_peak23_x = 412
start_peak33_x = 404
# Начальные координаты объектов мира по оси x

start_hand1_y = 388
start_hand2_y = 388
start_head_y = 350
start_leg1_y = 449
start_leg2_y = 449
start_puzo_y = 374

end_hand1_y = 340
end_hand2_y = 340
end_leg1_y = 410
end_leg2_y = 410
# Начальные координаты объектов человечка по оси y

start_stone_y = 50
start_speare_y = 449
start_speare_y1 = 475
start_peak11_y = 480
start_peak21_y = 480
start_peak31_y = 473

start_peak12_y = 445
start_peak22_y = 445
start_peak32_y = 438

start_peak13_y = 480
start_peak23_y = 480
start_peak33_y = 473

end_speare_y = 563
# Начальные координаты объектов мира по оси y

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Реализация выхода по крестику без зависаний

    screen.fill(VIOLET)
    # Установка фона

    pygame.draw.ellipse(screen, BLACK, [start_head_x, start_head_y, 25, 25])
    # Рисование головы
    pygame.draw.line(screen, BLACK, (start_hand1_x, start_hand1_y), (end_hand1_x, end_hand1_y))
    # Рисование руки 1
    pygame.draw.line(screen, BLACK, (start_hand2_x, start_hand2_y), (end_hand2_x, end_hand2_y))
    # Рисование руки 2
    pygame.draw.line(screen, BLACK, (start_leg1_x, start_leg1_y), (end_leg1_x, end_leg1_y))
    # Рисование ноги 1
    pygame.draw.line(screen, BLACK, (start_leg2_x, start_leg2_y), (end_leg2_x, end_leg2_y))
    # Рисование ноги 2
    pygame.draw.ellipse(screen, BLACK, [start_puzo_x, start_puzo_y, 25, 50])
    # Рисование тела

    pygame.draw.line(screen, RED, (368, start_speare_y1), (368, end_speare_y))
    pygame.draw.polygon(screen, RED, ((start_peak11_x, start_peak11_y),
                (start_peak21_x, start_peak21_y), (start_peak31_x, start_peak31_y)), 0)
    # Рисование копья 1
    pygame.draw.line(screen, RED, (386, start_speare_y), (386, end_speare_y))
    pygame.draw.polygon(screen, RED, ((start_peak12_x, start_peak12_y),
                (start_peak22_x, start_peak22_y), (start_peak32_x, start_peak32_y)), 0)
    # Рисование копья 2
    pygame.draw.line(screen, RED, (404, start_speare_y1), (404, end_speare_y))
    pygame.draw.polygon(screen, RED, ((start_peak13_x, start_peak13_y),
                (start_peak23_x, start_peak23_y), (start_peak33_x, start_peak33_y)), 0)
    # Рисование копья 3

    pygame.draw.ellipse(screen, BLACK, [start_stone_x, start_stone_y, 77, 77])
    # Рисование камня

    pygame.draw.ellipse(screen, GREY, [550, 15, 120, 120])
    # Рисование Луны
    pygame.draw.polygon(screen, BLACK, [(0, 500), (350, 500), (350, 449), (0, 449)])
    # Рисование границы 1
    pygame.draw.polygon(screen, BLACK, [(422, 500), (700, 500), (700, 449), (422, 449)])
    # Рисование границы 1

    start_hand1_x += speed_man_x
    start_hand2_x += speed_man_x
    start_head_x += speed_man_x
    start_leg1_x += speed_man_x
    start_leg2_x += speed_man_x
    start_puzo_x += speed_man_x

    end_hand1_x += speed_man_x
    end_hand2_x += speed_man_x
    end_leg1_x += speed_man_x
    end_leg2_x += speed_man_x
    # Передвижение человечка

    if end_speare_y < 547 or end_speare_y > 590:
        speed_speare *= -1
        speed_peaks *= -1
    # Движение копий вверх-вниз

    if start_stone_y >= 376 and start_stone_x < 346.48 :
        start_stone_x += speed_stone_x
        start_speare_y += speed_speare
        start_speare_y1 += speed_speare
        end_speare_y += speed_speare

        start_peak11_y += speed_peaks
        start_peak21_y += speed_peaks
        start_peak31_y += speed_peaks

        start_peak12_y += speed_peaks
        start_peak22_y += speed_peaks
        start_peak32_y += speed_peaks

        start_peak13_y += speed_peaks
        start_peak23_y += speed_peaks
        start_peak33_y += speed_peaks
    # Передвижение копий во время падения камня

    if start_stone_y < 376:
        start_stone_y += speed_stone_y
        start_speare_y += speed_speare
        start_speare_y1 += speed_speare
        end_speare_y += speed_speare

        start_peak11_y += speed_peaks
        start_peak21_y += speed_peaks
        start_peak31_y += speed_peaks

        start_peak12_y += speed_peaks
        start_peak22_y += speed_peaks
        start_peak32_y += speed_peaks

        start_peak13_y += speed_peaks
        start_peak23_y += speed_peaks
        start_peak33_y += speed_peaks
    # Передвижение копий и камня после его падения

    if 325 < start_puzo_x < 374:
        start_hand1_y += speed_man_y
        start_hand2_y += speed_man_y
        start_head_y += speed_man_y
        start_leg1_y += speed_man_y
        start_leg2_y += speed_man_y
        start_puzo_y += speed_man_y

        end_hand1_y += speed_man_y
        end_hand2_y += speed_man_y
        end_leg1_y += speed_man_y
        end_leg2_y += speed_man_y

    if 375 < start_puzo_x < 423.7:
        start_hand1_y -= speed_man_y
        start_hand2_y -= speed_man_y
        start_head_y -= speed_man_y
        start_leg1_y -= speed_man_y
        start_leg2_y -= speed_man_y
        start_puzo_y -= speed_man_y

        end_hand1_y -= speed_man_y
        end_hand2_y -= speed_man_y
        end_leg1_y -= speed_man_y
        end_leg2_y -= speed_man_y
    # Реализация "прыжка" через препятствие

    if start_stone_x >= 340 and 378 <= start_stone_y <= 430:
        start_stone_y += speed_stone_y
    # Падение камня в яму с копьями

    if start_hand1_x > 750:
        start_hand1_x = 15
        start_hand2_x = 37
        start_head_x = 15
        start_leg1_x = 10
        start_leg2_x = 46
        start_puzo_x = 15

        end_hand1_x = 0
        end_hand2_x = 52
        end_leg1_x = 18
        end_leg2_x = 35

        start_stone_x = 5
        start_peak11_x = 360
        start_peak21_x = 376
        start_peak31_x = 368

        start_peak12_x = 378
        start_peak22_x = 394
        start_peak32_x = 386

        start_peak13_x = 396
        start_peak23_x = 412
        start_peak33_x = 404

        start_hand1_y = 388
        start_hand2_y = 388
        start_head_y = 350
        start_leg1_y = 449
        start_leg2_y = 449
        start_puzo_y = 374

        end_hand1_y = 340
        end_hand2_y = 340
        end_leg1_y = 410
        end_leg2_y = 410

        start_stone_y = 50
        start_speare_y = 449
        start_speare_y1 = 475
        start_peak11_y = 480
        start_peak21_y = 480
        start_peak31_y = 473

        start_peak12_y = 445
        start_peak22_y = 445
        start_peak32_y = 438

        start_peak13_y = 480
        start_peak23_y = 480
        start_peak33_y = 473

        end_speare_y = 563
    # Реализация зацикливания

    pygame.display.flip()
    # Обновление экрана

    clock.tick(60)
    # Ограничение FPS

pygame.quit()
# Завершение