def main():
    M = int(input("輸入出生月份"))
    D = int(input("輸入出生日"))
    S = (M * 2 + D)%3
    
    if(S == 0):
        x = "普通"
    elif(S == 1):
        x = "吉"
    elif(S == 2):
        x = "大吉"

    print(x)
main()
