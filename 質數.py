def main():
    intnum = int(input("輸入正整數"))
    if(intnum == 1):
        print("不是質數")
    elif(intnum == 2):
        print("是質數")
    else:
        for i in range(2, intnum):
            if(intnum % i == 0):
                print("不是質數")
                break
        else:
            print("是質數")
main()