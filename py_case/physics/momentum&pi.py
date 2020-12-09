def collision(m1, v1, m2, v2):
    va = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)
    vb = (v2 * (m2 - m1) + 2 * m1 * v1) / (m2 + m1)
    return va, vb


def func_times(m1, v1, m2, v2):
    times = 0
    while (True):
        if (v1 < 0 and v2 <= 0 and abs(v1) >= abs(v2)):
            break
        v1, v2 = collision(m1, v1, m2, v2)
        times = times + 1

        if (v1 < 0 and v2 <= 0 and abs(v1) >= abs(v2)):
            break

        v2 = -1 * v2
        times = times + 1

    return times


m1 = 100
m2 = 100
v1 = 100
v2 = 0
for _ in range(0, 7):
        m1 = m1*100
        times = func_times(m1, v1, m2, v2)
        print(f"M1:{m1}, M2:{m2}, v1:{v1}, v2:{v2}, Times:{times}")
