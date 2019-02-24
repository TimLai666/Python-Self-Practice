def main():
    money = int(input("輸入購物金額"))
    newmoney = moneyoff(money)
    print("請付", newmoney, "元")
    
    
def moneyoff(money):
    if(money >= 100000):
        money *= 0.8
    elif(money >= 50000):
        money *= 0.85
    elif(money >= 30000):
        money *= 0.9
    elif(money >= 10000):
        money *= 0.95
        
    return money
main()