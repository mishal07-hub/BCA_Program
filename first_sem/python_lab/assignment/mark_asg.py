python=int(input("enter python marks:"))
math=int(input("enter math mark:"))
computer=int(input("enter computer mark:"))
if python>=0 and python<=100:
    if math>=0 and math<=100:
        if computer>=0 and computer<=100:
            total=python+math+computer
            print("total:",total)
            average=total/3
            print("average:",round(average,2))
            percentage=(total/300)*100
            print("percentage:",round(percentage,2),"%")
            if percentage>=70:
                print("distinction")
            elif percentage>=60:
                print("first class")
            elif percentage>=40:
                print("second class")
            else:
                print("fail")
        else:
            print("invalid value")
    else:
        print("invalid value")
else:
    print("invalid value")