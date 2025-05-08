# Feito por Miguel Almeida Morais no dia 1 de Junho de 2023.


def centrar(x, y):
    if 150 < x < 250:
        if 400 < y < 500:
            return 200, 450
        if 300 < y < 400:
            return 200, 350
        if 200 < y < 300:
            return 200, 250
    elif 250 < x < 350:
        if 400 < y < 500:
            return 300, 450
        if 300 < y < 400:
            return 300, 350
        if 200 < y < 300:
            return 300, 250
    elif 350 < x < 450:
        if 400 < y < 500:
            return 400, 450
        if 300 < y < 400:
            return 400, 350
        if 200 < y < 300:
            return 400, 250
