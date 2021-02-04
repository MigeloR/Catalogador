def a():
    b = ("1", "2")
    c = range(2)
    e = ("11", "22")
    n = 0
    for i in e:
        print(f"b es {b[n]} y e es {e[n]}")
        n += 1


if __name__ == '__main__':
    a()