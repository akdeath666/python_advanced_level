import random

money=0
print("WELCOME TO KBC, KAUN BANEGA CROREPATI")
print("HERE, WE WILL PROVIDE QUESTIONS AND BY ANSWERING THEM CORRECTLY YOU CAN WIN CASH PRIZES\n"\
      "SO LETS GET STARTED")

#LIST OF QUESTIONS
question={0:'WHICH RIVER IS KNOWN AS SORROW OF BENGAL?',1:'WHICH IS THE MOST POPULAR SPORT ALL OVER THE WORLD?',
          2:'WHICH COUNTRY HAS WON THE FIRST CRICKET WORLD CUP?',3:'WHO IS THE PRESIDENT OF USA CURRENTLY?',
          4:'QUEEN MARY WAS A POPULAR RULER OF WHICH OF THE FOLLOWING COUNTRIES?'}
#LIST OF OPTIONS
option1=['RAFTI','DAMODAR','BRAHMAPUTRA','GODAVARI']
option2=['CRICKET','FOOTBALL','RUGBY','HOCKEY']
option3=['INDIA','AUSTRALIA','ENGLAND','WEST INDIES']
option4=['BLADIMIR PUTIN','NARENDRA MODI','DONALD TRUMPH','TRENT BOULT']
option5=['ENGLAND','NEW ZEALAND','INDIA','GERMANY']

#LIST OF CORRECT OPTIONS
correct=['DAMODAR','FOOTBALL','WEST INDIES','DONALD TRUMPH','ENGLAND']

#CODING STARTS
for i in range(0,len(question)):
    print("THIS QUESTION IS FOR ",money+2000000)

    #HERE WE ARE ACCEPTING RANDOM KEY
    key=random.choice(list(question.keys()))
    ques=question[key]
    print(ques)

    if(key==0):
        A=random.choice(option1)
        option1.remove(A)
        B=random.choice(option1)
        option1.remove(B)
        C=random.choice(option1)
        option1.remove(C)
        D=random.choice(option1)
        option1.remove(D)
        corr=correct[0]

        print("A:", A)
        print("B:", B)
        print("C:", C)
        print("D:", D)

        choice=input("ENTER YOUR CHOICE:")

        if((corr==A and choice=='A') or (corr==B and choice=='B') or (corr==C and choice=='C') or (corr==D and choice=='D')):
            money=money+2000000
            print("CONGRATULATIONS,YOU WIN ",money)
            ch=int(input("DO YOU WANT TO CONTINUE,YES=1/NO=0, ONLY AT YOUR RISK\n"))

            if(ch==0):
                print("YOUR SUM IS: ",money)
                print("GOOD BYE")
                break

        else:
            print("SORRY,YOU LOSE.\n"\
                  "YOUR SUM IS: ",money)
            break



    elif(key==1):
        A=random.choice(option2)
        option2.remove(A)
        B=random.choice(option2)
        option2.remove(B)
        C=random.choice(option2)
        option2.remove(C)
        D=random.choice(option2)
        option2.remove(D)
        corr=correct[1]

        print("A:", A)
        print("B:", B)
        print("C:", C)
        print("D:", D)

        choice=input("ENTER YOUR CHOICE: ")

        if((corr==A and choice=='A') or (corr==B and choice=='B') or (corr==C and choice=='C') or (corr==D and choice=='D')):
            money=money+2000000
            print("CONGRATULATIONS,YOU WIN ",money)
            ch=int(input("DO YOU WANT TO CONTINUE,YES=1/NO=0, ONLY AT YOUR RISK\n"))

            if(ch==0):
                print("YOUR SUM IS: ",money)
                print("GOOD BYE")
                break

        else:
            print("SORRY,YOU LOSE.\n"\
                  "YOUR SUM IS: ",money)
            break

    elif(key==2):
        A=random.choice(option3)
        option3.remove(A)
        B=random.choice(option3)
        option3.remove(B)
        C=random.choice(option3)
        option3.remove(C)
        D=random.choice(option3)
        option3.remove(D)
        corr=correct[2]

        print("A:", A)
        print("B:", B)
        print("C:", C)
        print("D:", D)

        choice=input("ENTER YOUR CHOICE: ")

        if((corr==A and choice=='A') or (corr==B and choice=='B') or (corr==C and choice=='C') or (corr==D and choice=='D')):
            money=money+2000000
            print("CONGRATULATIONS,YOU WIN ",money)
            ch=int(input("DO YOU WANT TO CONTINUE,YES=1/NO=0, ONLY AT YOUR RISK\n"))

            if(ch==0):
                print("YOUR SUM IS: ",money)
                print("GOOD BYE")
                break

        else:
            print("SORRY,YOU LOSE.\n"\
                  "YOUR SUM IS: ",money)
            break

    elif(key==3):
        A=random.choice(option4)
        option4.remove(A)
        B=random.choice(option4)
        option4.remove(B)
        C=random.choice(option4)
        option4.remove(C)
        D=random.choice(option4)
        option4.remove(D)
        corr=correct[3]

        print("A:", A)
        print("B:", B)
        print("C:", C)
        print("D:", D)

        choice=input("ENTER YOUR CHOICE: ")

        if((corr==A and choice=='A') or (corr==B and choice=='B') or (corr==C and choice=='C') or (corr==D and choice=='D')):
            money=money+2000000
            print("CONGRATULATIONS,YOU WIN ",money)
            ch=int(input("DO YOU WANT TO CONTINUE,YES=1/NO=0, ONLY AT YOUR RISK\n"))

            if(ch==0):
                print("YOUR SUM IS: ",money)
                print("GOOD BYE")
                break

        else:
            print("SORRY,YOU LOSE.\n"\
                  "YOUR SUM IS: ",money)
            break


    elif(key==4):
        A=random.choice(option5)
        option5.remove(A)
        B=random.choice(option5)
        option5.remove(B)
        C=random.choice(option5)
        option5.remove(C)
        D=random.choice(option5)
        option5.remove(D)
        corr=correct[4]

        print("A:", A)
        print("B:", B)
        print("C:", C)
        print("D:", D)

        choice=input("ENTER YOUR CHOICE: ")

        if((corr==A and choice=='A') or (corr==B and choice=='B') or (corr==C and choice=='C') or (corr==D and choice=='D')):
            money=money+2000000
            print("CONGRATULATIONS,YOU WIN ",money)
            ch=int(input("DO YOU WANT TO CONTINUE,YES=1/NO=0, ONLY AT YOUR RISK\n"))

            if(ch==0):
                print("YOUR SUM IS: ",money)
                print("GOOD BYE")
                break

        else:
            print("SORRY,YOU LOSE.\n"\
                  "YOUR SUM IS: ",money)
            break
    del question[key]
    


    


    