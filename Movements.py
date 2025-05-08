# Feito por Miguel Almeida Morais no dia 1 de Junho de 2023.


def movcavalo(x, y):
    if (x == 200 and y == 100) or (x == 100 and y == 200):
        return True
    else:
        return False


def movbispo(x, y):
    if x == y or x == -y:
        return True
    else:
        return False


def movtorre(x, y):
    if x == 0 or y == 0:
        return True
    else:
        return False

