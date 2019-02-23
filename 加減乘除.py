def main():
    total = 0
    how = input("輸入運算符號")
    
    if(how == "+"):
        total = add()
    elif(how == "-"):
        total = mi()
    elif(how == "*"):
        total = mu()
    elif(how == "/"):
        total = di()
 
    print("總和:", total)


# +
def add():
    total = 0
    num = 0
    
    while(1 > 0):
        num = int(input("輸入數字"))
        if(num == 0):
            break
        else:
            total += num
    
    return total


# -
def mi():
    total = 0
    num = 0
    i = 0
    
    while(1 > 0):
        num = int(input("輸入數字"))
        if(i == 0):
            total = num
            i += 1
            continue
        
        if(num == 0):
            break
        else:
            total -= num
    
    return total


# *
def mu():
    total = 1
    num = 0
    
    while(1 > 0):
        num = int(input("輸入數字"))
        if(num == 0):
            break
        else:
            total *= num
    
    return total


# /
def di():
    total = 0
    num = 0
    i = 0
    
    while(1 > 0):
        num = int(input("輸入數字"))
        if(i == 0):
            total = num
            i += 1
            continue
        
        if(num == 0):
            break
        else:
            total /= num
    
    return total


main()
