import random

PC_score = 0
USER_score = 0
inning_num = 0 # 매개변수 이닝: 함수 내에서 변하는 수

# 공수교대 한 후 다시 공격을 때 base에 있던 사람들이 다 초기화되어있음.
# base 임시 저장 공간
global temporary_storage_Base_1
global temporary_storage_Base_2
temporary_storage_Base_1 = 0
temporary_storage_Base_2 = 0

inning = 2*(3) # 사용자 지정 상수 이닝: (1이닝) (2이닝) (3이닝) 
strike_out = 3 # 사용자 지정 상수 strike out 값. ex) 값이 1이면, 1strike --> 1out

# 확률 함수
# 0 큰 확률로 걸림, 1 작은 확률로 정해짐 ex) 70퍼로 걸리면 0, 30퍼로 걸리면 1
def percentage_3vs7():
    S_or_B = 0 
    percent=random.randrange(1,11)
    if (percent >= 1 and percent <=3):
        S_or_B = 1
    
    return S_or_B

# 1~4 스윙 --> 1~4, 5~7 스윙안함 --> 0
def percentage_PC_Hitter():
    result = 0
    percent_H = random.randrange(1,8)
    if (percent_H >= 1 and percent_H <=4):
        result = percent_H

    return result

# 1~4 strike --> 1~4, 5~7 ball존 --> 0
def percentage_PC_Pitcher():
    result = 0
    percent_P = random.randrange(1,8)
    if (percent_P >= 1 and percent_P <=4):
        result = percent_P

    return result



def print_P_S_Position(P, S):
    # print("Picher: %d, Swing: %d" % (P, S)) # 수치 확인

    L = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

    if (P == 0): 
        random_Pitch_position = random.randrange(1,4)
        if (random_Pitch_position == 1):
            L[1][0] = 'O'
        elif (random_Pitch_position == 2):
            L[1][1] = 'O'
        elif (random_Pitch_position == 3):
            L[1][2] = 'O'
        elif (random_Pitch_position == 4):
            L[1][3] = 'O'

        if (S >= 1 and S <= 4):
            L[0][S-1] = 'X'
    elif (S ==  P and S != 0):
        L[0][S-1] = '%'
    else:
        L[0][P-1] = 'O'
        if (S == 0):
            L[0][P-1] = 'O'
        else:
            L[0][S-1] = 'X'

    print("   %s\n  -----\n  |%s %s|  %s\n%s |%s %s|\n  -----\n     %s" % (L[1][0], L[0][0], L[0][1], L[1][1], L[1][2], L[0][2], L[0][3], L[1][3]))


def print_innig(inning_num):
    print('\n####################%d회####################' % (inning_num/2 + 1))
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
    global temporary_storage_Base_1
    base = temporary_storage_Base_1 # 전 공격 떄 base를 복원

    strike = 0
    out = 0
    ball = 0
    
    
    #print("base: %d" % base) # base 저장된 것 확인
    print_innig(inning_num) # 몇회인지, 전반또는 후반인지 출력
    print("\n당신은 Hitter(타자) 입니다!\n")

    while(True):
        

        PC_Picher = percentage_PC_Pitcher()
        # print("PC_Picher: ", PC_Picher) # 컴_투수 위치
        print("스윙할 위치를 선택하세요")
        Swing = int(input("(not Swing: 0, Swing: 1~4): "))
        
        
        print("")
        # 투수 던진위치, 타자 친 위치 같이 출력
        print_P_S_Position(PC_Picher, Swing)
        print("")

        # ball, homelearn, out, safety 판정
        if(Swing == 0 and PC_Picher == 0): 
            ball += 1
            print("ball!")
        elif(Swing == PC_Picher and Swing != 0):
            S_or_H = percentage_3vs7()
            # print("percentage: ", S_or_H) # 오류 검사
            if (S_or_H == 0):
                base += 1
                strike = 0
                ball = 0
                print("safety!! 1루 진출!")
            elif (S_or_H == 1):
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
        #print("base: %d, score: %d" % (base, USER_score)) # base, score 적용되었는지 확인
        print("")

        #결과 출력
        print_Score(USER_score, PC_score)
        print("USER") # 공격수 구분
        print_Result(strike, ball, out)

        if(out == 3):
            temporary_storage_Base_1 = base # 전 공격 때 base를 보관
            #print("temporary_storage_Base_1: %d" % temporary_storage_Base_1) # 저장 확인
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
    global temporary_storage_Base_2
    base = temporary_storage_Base_2 # 전 공격 떄 base를 복원

    strike = 0
    out = 0
    ball = 0
    
    #print("base: %d" % base) # base 저장된 것 확인
    print_innig(inning_num) # 몇회인지, 전반또는 후반인지 출력
    print("\n당신은 Picher(투수) 입니다!\n")
        

    while(True):
        
        PC_Hitter = percentage_PC_Hitter()
        # print("PC_Hitter: ", PC_Hitter) # 컴_타자 위치
        print("타자에게 던질 위치를 선택하세요")
        Picher = int(input("(ball zone: 0, strike zone: 1~4): "))

        print("")
        # 투수 던진위치, 타자 친 위치 같이 출력
        print_P_S_Position(Picher, PC_Hitter)
        print("")

        # ball, homelearn, out, safety 판정
        if(PC_Hitter == 0 and Picher == 0): 
            ball += 1
            print("ball!")
        elif(PC_Hitter == Picher and PC_Hitter != 0):
            S_or_H = percentage_3vs7()
            # print("percentage: ", S_or_H) # 오류 검사
            if (S_or_H == 0):
                base += 1
                strike = 0
                ball = 0
                print("safety!! 1루 진출")
            elif (S_or_H == 1):
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
        #print("base: %d, score: %d" % (base, PC_score)) # base, score 적용되었는지 확인
        print("")

        #결과 출력
        print_Score(USER_score, PC_score)
        print("PC") # 공격수 구분
        print_Result(strike, ball, out)

        if(out == 3):
            temporary_storage_Base_2 = base # 전 공격 때 base를 보관
            #print("temporary_storage_Base_2: %d" % temporary_storage_Base_2) # 저장된 것 확인
            inning_num += 1
            if(inning_num == inning): # 2: 1이닝,  4: 2이닝, 6: 3이닝
                print("\n")
                print_Winner(USER_score, PC_score) # 승자 판별 후 출력
                
                exit() # 프로그램 종료

            print("\n########################")
            print("#이닝 종료!! 공수교대!!#")
            print("########################")
            Hitter(USER_score, PC_score, inning_num)

def Start_Baseballgame():
    print("=====start baseballgame=====")
    select = input("choice attack or defend (a, d): ")

    if(select == 'a' or select == 'A'):
        Hitter(USER_score, PC_score, inning_num)
    elif(select == 'd' or select == 'D'):
        Picher(USER_score, PC_score, inning_num)


Start_Baseballgame()
