import random
#1부터 100까지 난수 입력
numb=random.randrange(1,101,1)
num = -1

numb_total = 0

print("게임시작")

#숫자 넣기
while(numb != num):
    num = int(input("1~100사이의 숫자를 입력하시오:"))

    if(num>numb):
        print("down")
    elif(num<numb):
        print("up")
    numb_total+=1
print(numb_total, "번만에 정답을 맞추셨습니다.")
