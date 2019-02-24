def main():
    ans = 0
    for i  in range(1, 9 + 1):
        for j in range(1, 9 + 1):
            ans = i * j
            print(i, "*", j, "=", ans)
        print()
main()