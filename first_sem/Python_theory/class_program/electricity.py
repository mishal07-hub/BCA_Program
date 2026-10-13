unit=int(input("unit:"))
threshold=input("threshold:")
category=input("category:")
date=input("date:")
if unit<=100:
    if category=="commercial":
        if threshold=="yes":
            amount=(unit*10)+100
            print("the amount=",amount)
        else:
            amount=(unit*10)
            print("the amount=",amount)
    if category=="non commercial":
        if threshold=="yes":
            amount=(unit*5)+50
            print("the amount=",amount)
        else:
            amount=(unit*5)
            print("the amount=",amount)
elif unit>300:
    if category=="commercial":
        if threshold=="yes":
            amount=(unit*12)+100
            print("the amount=",amount)
        else:
            amount=(unit-100)*15
            print("the amount=",amount)
    if category=="non commercial":
        if threshold=="yes":
            amount=(unit)*8+50
            print("the amount=",amount)
        else:
            amount=((unit)*8)
            print("the amount=",amount)
else:
    if category=="commercial":
            if threshold=="yes":
                amount=(unit)*12+100
                print("the amount=",amount)
            else:
                amount=(unit)*15
                print("the amount=",amount)
    if category=="non commercial":
            if threshold=="yes":
                amount=(unit)*6+50
                print("the amount=",amount)
            else:
                amount=(unit-100)*6
                print("the amount=",amount)

