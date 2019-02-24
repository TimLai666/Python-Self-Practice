def main():
    a = f()
    out(a)


def f():
    a = 1 + 2 * 3
    return a

def out(a):
    print("1+2*3=", a)

main()
