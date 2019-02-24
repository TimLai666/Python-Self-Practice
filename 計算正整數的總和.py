def main():
    n = int(input("輸入正整數"))
    total = 0
    for i in range(1, n + 1):
        total += i
    print("總和為:", total)
main()