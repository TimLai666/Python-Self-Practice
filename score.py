def main():
    score = []
    scoren = 0
    i = 0
    total = 0
    while(scoren != -1):
        i += 1
        print("輸入成績", i, ":", end = "")
        scoren = int(input())
        if(scoren == -1):
            i -= 1
            break
        score.append(scoren)
        
    for j in range(i):
        total += score[j]
    average = total / i
    
    score.sort()
    score.reverse()
    print("成績依序為:")
    for j in range(i):
        print(score[j])
    
    print("總分為:", total)
    print("平均:", average)
    
main()
