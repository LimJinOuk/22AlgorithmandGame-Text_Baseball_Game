import random

PC_score = 0
USER_score = 0
inning_num = 0 # 매개변수 이닝: 함수 내에서 변하는 수

inning = 2*(3) # 사용자 지정 상수 이닝: (1이닝) (2이닝) (3이닝) 
strike_out = 1 # 사용자 지정 상수 strike out 값. ex) 값이 1이면, 1strike --> 1out

# 확률 함수
# 0 큰 확률로 걸림, 1 작은 확률로 정해짐 ex) 70퍼로 걸리면 0, 30퍼로 걸리면 1
def percentage_3vs7():
    S_or_B = 0 # 0 큰 확률로 걸림, 1 작은 확률로 정해짐 ex) 70퍼로 걸리면 0, 30퍼로 걸리면 1
    percent=random.randrange(1,11)
    if (percent >= 1 and percent <=3):
        S_or_B = 1
    
    return S_or_B



def print_innig(inning_num):
    print('\n####################%d회####################' % (inning_num/2 + 1)) # 수정하기
    if(inning_num % 2 == 0):
        print("####################전반###################")
    else:
        print("####################후반###################")

def print_Score(U_s, P_s):
    print("==========================")
    print("        USER : PC")
    print("           %d : %d" % (U_s,P_s))
    print("==========================")

def print_Result(s, b, o):
    print("  %d strike  %d ball  %d out" % (s, b, o))
    print("==========================")

def print_Winner(USER_score, PC_score):
    if(USER_score > PC_score):
        print("당신이 이겼습니다!")
    elif(USER_score < PC_score):
        print("당신이 졌어요...")
    elif(USER_score == PC_score):
        print("무승부 입니다!")

def Hitter(USER_score, PC_score, inning_num):

    strike = 0
    out = 0
    ball = 0
    base = 0
    
    print_innig(inning_num) # 몇회인지, 전반또는 후반인지 출력
    print("\n당신은 Hitter(타자) 입니다!\n")

    while(True):
        

        PC_Picher = random.randrange(0,10)
        print("PC_Picher: ", PC_Picher) # 컴_투수 위치
        print("스윙할 위치를 선택하세요")
        Swing = int(input("(not Swing: 0, Swing: 1~9): "))
        
        
        print("")
        # 투수가 던진 위치
        if(PC_Picher == 1):
            print("-------\n|O    |\n|     |\n|     |\n-------")
        elif(PC_Picher == 2):
            print("-------\n|  O  |\n|     |\n|     |\n-------")
        elif(PC_Picher == 3):
            print("-------\n|    O|\n|     |\n|     |\n-------")
        elif(PC_Picher == 4):
            print("-------\n|     |\n|O    |\n|     |\n-------")    
        elif(PC_Picher == 5):
            print("-------\n|     |\n|  O  |\n|     |\n-------")            
        elif(PC_Picher == 6):
            print("-------\n|     |\n|    O|\n|     |\n-------")
        elif(PC_Picher == 7):
            print("-------\n|     |\n|     |\n|O    |\n-------")   
        elif(PC_Picher == 8):
            print("-------\n|     |\n|     |\n|  O  |\n-------")
        elif(PC_Picher == 9):
            print("-------\n|     |\n|     |\n|    O|\n-------")      
        else:
            print("-------\n|     |\n|     |\n|     |\n-------") 
        # 타자가 친 위치
        if(Swing == 1):
            print("-------\n|X    |\n|     |\n|     |\n-------")
        elif(Swing == 2):
            print("-------\n|  X  |\n|     |\n|     |\n-------")
        elif(Swing == 3):
            print("-------\n|    X|\n|     |\n|     |\n-------")
        elif(Swing == 4):
            print("-------\n|     |\n|X    |\n|     |\n-------")    
        elif(Swing == 5):
            print("-------\n|     |\n|  X  |\n|     |\n-------")            
        elif(Swing == 6):
            print("-------\n|     |\n|    X|\n|     |\n-------")
        elif(Swing == 7):
            print("-------\n|     |\n|     |\n|X    |\n-------")   
        elif(Swing == 8):
            print("-------\n|     |\n|     |\n|  X  |\n-------")
        elif(Swing == 9):
            print("-------\n|     |\n|     |\n|    X|\n-------")     
        else:
            print("-------\n|     |\n|     |\n|     |\n-------")  
        print("")
        
        # ball, homelearn, out, safety 판정
        if(Swing == 0 and PC_Picher == 0): 
            ball += 1
            print("ball!")
        elif(Swing == PC_Picher and Swing != 0):
            S_of_H = percentage_3vs7()
            print("percentage: ", S_of_H) # 오류 검사
            if (S_of_H == 0):
                base += 1
                strike = 0
                ball = 0
                print("safety!! 1루 진출!")
            elif (S_of_H == 1):
                USER_score = USER_score + base + 1
                strike = 0
                ball = 0
                base = 0
                print("HomeLearn!!")
        else:
            strike +=1
            print("strike!")
       


        if(strike == strike_out): ## 실행시간 절약
            out += 1
            strike = 0
            ball = 0
            print("out!!")
       
        if(ball == 4):
            base += 1
            strike = 0
            ball = 0
            print("ball 4번! 1루 진출!")
        
        print("")
        #base 출력 (함수로 만들면 지역변수 때문에 점수가 안오름)
        if(base == 0):
            print("     △   \n\n◁         ▷\n\n     ◇")
        elif(base == 1):
            print("     △   \n\n◁         @\n\n     ◇")
        elif(base == 2):
            print("     @    \n\n◁         @\n\n     ◇")
        elif(base == 3):
            print("     @    \n\n@         @\n\n     ◇")
        elif(base == 4):
            base -= 1
            USER_score += 1
            print("     @    \n\n@         @\n\n     ◇")
        print("base: %d, score: %d" % (base, USER_score)) # base, score 적용되었는지 확인
        print("")

        #결과 출력
        print_Score(USER_score, PC_score)
        print("USER") # 공격수 구분
        print_Result(strike, ball, out)

        if(out == 3):
            inning_num += 1
            if(inning_num == inning): # 2: 1이닝,  4: 2이닝, 6: 3이닝
                print("\n")
                print_Winner(USER_score, PC_score) # 승자 판별 후 출력

                exit() # 프로그램 종료

            print("\n########################")
            print("#이닝 종료!! 공수교대!!#")
            print("########################")
            Picher(USER_score, PC_score, inning_num)


def Picher(USER_score, PC_score, inning_num):

    strike = 0
    out = 0
    ball = 0
    base = 0
    
    print_innig(inning_num) # 몇회인지, 전반또는 후반인지 출력
    print("\n당신은 Picher(투수) 입니다!\n")
    #print("123\n456\n789\n")    

    while(True):
        
        PC_Hitter = random.randrange(0,10)
        print("PC_Hitter: ", PC_Hitter) # 컴_타자 위치
        print("타자에게 던질 위치를 선택하세요")
        Picher = int(input("(ball zone: 0, strike zone: 1~9): "))

        print("")
        # 투수가 던진 위치
        if(Picher == 1):
            print("-------\n|O    |\n|     |\n|     |\n-------")
        elif(Picher == 2):
            print("-------\n|  O  |\n|     |\n|     |\n-------")
        elif(Picher == 3):
            print("-------\n|    O|\n|     |\n|     |\n-------")
        elif(Picher == 4):
            print("-------\n|     |\n|O    |\n|     |\n-------")    
        elif(Picher == 5):
            print("-------\n|     |\n|  O  |\n|     |\n-------")            
        elif(Picher == 6):
            print("-------\n|     |\n|    O|\n|     |\n-------")
        elif(Picher == 7):
            print("-------\n|     |\n|     |\n|O    |\n-------")   
        elif(Picher == 8):
            print("-------\n|     |\n|     |\n|  O  |\n-------")
        elif(Picher == 9):
            print("-------\n|     |\n|     |\n|    O|\n-------")      
        else:
            print("-------\n|     |\n|     |\n|     |\n-------")
        # 타자가 친 위치
        if(PC_Hitter == 1):
            print("-------\n|X    |\n|     |\n|     |\n-------")
        elif(PC_Hitter == 2):
            print("-------\n|  X  |\n|     |\n|     |\n-------")
        elif(PC_Hitter == 3):
            print("-------\n|    X|\n|     |\n|     |\n-------")
        elif(PC_Hitter == 4):
            print("-------\n|     |\n|X    |\n|     |\n-------")    
        elif(PC_Hitter == 5):
            print("-------\n|     |\n|  X  |\n|     |\n-------")            
        elif(PC_Hitter == 6):
            print("-------\n|     |\n|    X|\n|     |\n-------")
        elif(PC_Hitter == 7):
            print("-------\n|     |\n|     |\n|X    |\n-------")   
        elif(PC_Hitter == 8):
            print("-------\n|     |\n|     |\n|  X  |\n-------")
        elif(PC_Hitter == 9):
            print("-------\n|     |\n|     |\n|    X|\n-------")     
        else:
            print("-------\n|     |\n|     |\n|     |\n-------")    
        print("")

        # ball, homelearn, out, safety 판정
        if(PC_Hitter == 0 and Picher == 0): 
            ball += 1
            print("ball!")
        elif(PC_Hitter == Picher and PC_Hitter != 0):
            S_of_H = percentage_3vs7()
            print("percentage: ", S_of_H) # 오류 검사
            if (S_of_H == 0):
                base += 1
                strike = 0
                ball = 0
                print("safety!! 1루 진출")
            elif (S_of_H == 1):
                PC_score = PC_score + base + 1
                strike = 0
                ball = 0
                base = 0
                print("HomeLearn!!")
        else:
            strike += 1
            print("strike!")




        if(strike == strike_out): ## 실행시간 절약
            out += 1
            strike = 0
            ball = 0
            print("out!!")

        if(ball == 4):
            base += 1 
            strike = 0          
            ball = 0
            print("ball 4번! 1루 진출!")

        print("") 
        #base 출력 (함수로 만들면 지역변수 때문에 점수가 안오름)
        if(base == 0):
            print("     △   \n\n◁         ▷\n\n     ◇")
        elif(base == 1):
            print("     △   \n\n◁         @\n\n     ◇")
        elif(base == 2):
            print("     @    \n\n◁         @\n\n     ◇")
        elif(base == 3):
            print("     @    \n\n@         @\n\n     ◇")
        elif(base == 4):
            base -= 1
            PC_score += 1
            print("     @    \n\n@         @\n\n     ◇")
        print("base: %d, score: %d" % (base, PC_score)) # base, score 적용되었는지 확인
        print("")

        #결과 출력
        print_Score(USER_score, PC_score)
        print("PC") # 공격수 구분
        print_Result(strike, ball, out)

        if(out == 3):
            inning_num += 1
            if(inning_num == inning): # 2: 1이닝,  4: 2이닝, 6: 3이닝
                print("\n")
                print_Winner(USER_score, PC_score) # 승자 판별 후 출력
                
                exit() # 프로그램 종료

            print("\n########################")
            print("#이닝 종료!! 공수교대!!#")
            print("########################")
            Hitter(USER_score, PC_score, inning_num)


print("=====start baseballgame=====")
select = input("choice attack or defend (a, d): ")

if(select == 'a' or select == 'A'):
    Hitter(USER_score, PC_score, inning_num)
elif(select == 'd' or select == 'D'):
    Picher(USER_score, PC_score, inning_num)
