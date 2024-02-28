def multiplication(a, b):
    if b < 0:
        b = -b
        a = -a

    somme = 0
    for i in range(b):
        somme += a

    return somme


# Tests
assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(3, -4) == -12
assert multiplication(-2, 0) == 0

