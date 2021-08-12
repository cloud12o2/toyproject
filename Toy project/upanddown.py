import random
#1부터 100까지 난수 입력
numb=random.randrange(1,101,1)
pnum = -1

numb_total = 0

print("게임시작")

#숫자 넣기

while(numb != pnum):
        num = int(input("1~100사이의 숫자를 입력하시오:"))

        if (numb_total > 3):
            print("5번 시도하셨슴당 게임오버")
            break

        if(pnum>numb):
          print("down")
        elif(pnum<numb):
          print("up")
          numb_total += 1

            #print(numb_total, "번만에 정답을 맞추셨습니다.")
