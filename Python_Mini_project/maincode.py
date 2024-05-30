import random
print()
print("\t\tWelcome to Kaun Banega Crorepati")
a=input("\t   Enter Player Name -")
print("\n\t\tTo",a, "Chaliye Shuru Karte Hain\n")
questions=["nagpur is famous for","Where is the only diamond crossing in India located","YCCE is also known as","India's first textile mill is located in which city","Geographical center of India"]
answer=["Oranges","Nagpur","IIT Wanadongri","Nagpur","Nagpur"]
Wronganswers=[["Mangoes","Grapes","Apples"],["Wardha","Pune","Mumbai"],["NIT Wanadongri","IIIT Wanadongri"],["Pune","Wardha","Mumbai"],["Wardha","Pune","Mumbai"]]
attempt=[]
count=1
money=0
while True:
    while True:
        sel=random.choice(questions)
        if sel in attempt:
            pass
        elif sel not in attempt:
            attempt.append(sel) 
            questionindex=questions.index(sel)
            correctanswer=answer[questionindex]
            break
        options=[]
        option1=[]
        optioncount=1
        while optioncount<4:
            optionsel=random.choice(Wronganswers[questionindex])
            if optionsel in option1:
                pass
            elif optionsel not in option1:
                options.append(optionsel)
                option1.append(optionsel)
                optioncount+=1
        options.append(correctanswer)
        alreadydisplay=[]
        optiontodisplay=[]
        a1=True
        while a1:
            a=random.choice(options)
            if a in alreadydisplay:
                pass
            else:
                alreadydisplay.append(a)
                optiontodisplay.append(a)
                a1=not True
        a1=True
        while a1:
            b=random.choice(options)
            if b in alreadydisplay:
                pass
            else:
                alreadydisplay.append(b)
                optiontodisplay.append(b)
                a1=not True
        a1=True
        while a1:
            c=random.choice(options)
            if c in alreadydisplay:
                pass
            else:
                alreadydisplay.append(c)
                optiontodisplay.append(c)
                a1=not True
        a1=True
        while a1:
            d=random.choice(options)
            if d in alreadydisplay:
                pass
            else:
                alreadydisplay.append(d)
                optiontodisplay.append(d)
                a1=not True
        right_answer=""
        if correctanswer==a:
            right_answer="a"
        elif correctanswer==b:
            right_answer="b"
        elif correctanswer==c:
            right_answer="c"
        elif correctanswer==d:
            right_answer="d"
        print("\t\t\tMoney Win - ",money)
        print("\n\t\tQuestion ",count,"Aapki Screen pe\n\n")
        print("  Question - ",sel)
        print("\t A. ",a)
        print("\t B. ",b)
        print("\t C. ",c)
        print("\t D. ",d)
        useranswer=input("\t\tEnter correct option\t or \t press Q to quit.\n\t\t\t>>>").lower()
        if useranswer==right_answer:
            if count==1:
                money=10000
            elif count==2:
                money=20000
            elif count==3:
                money=50000
            elif count==4:
                money=7500000
            elif count==5:
                money=150000000
                print("\n\n\n")
                print("\t\t\t <<<<< Adbhut* >>>>>")
                print("\t\t\\\\\\ Badhai Ho Aap Crorepati Ban Chuke Hai /////")
                print("\n\n\t\t\t Aap Jite hai Rs ",money)
                print()
                break
            print("\n\n\n")
            print("\t\t\t <<<<< Abhinandan* >>>>>")
            print("\t\t\t\\\\\\ Sahi Jawab //////")
            count+=1
        elif useranswer=="q":
            print("\n\n\t\t\tAap Jite hai Rs. ",money)
            break
        else:
            print("\t\t\tGalat Jawab")
            print("\n\n\t\t \tAap Jite Hai Rs. ",money)
            break

