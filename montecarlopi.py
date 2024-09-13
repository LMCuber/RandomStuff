from random import uniform as randf


def generate():
    return randf(0, 1), randf(0, 1)


con = di = 0
for _ in range(100_000_0):
    x, y = generate()
    if x ** 2 + y ** 2 <= 1:
        con += 1
    else:
        di += 1
    pi_approx = con / (con + di) * 4
print(pi_approx)
