def main():
    n = int(input("輸入成績數量:"))
    score = []
    
    for i in range(n):
        print("輸入成績", i + 1, ":", end = "")
        scorenum = int(input())
        score.append(scorenum)
    add(score, n)

    
def add(score, n):
    total = 0
    for i in range(n):
        total += score[i]
    print("總分:", total)
    average(total, n)


def average(total, n):
    a = total / n
    print("平均:", a)
main()
