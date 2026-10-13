age=int (input("age:"))
day=input("day:")
show=input("show timing:")
price=250
if day=="weekend":
    if show=="morning show":
        if age<=5:
            amount=price*(50/100)*(125/100)
            print("ticket price=",amount)
        elif age>=60:
            amount=price*(90/100)*(125/100)
            print("ticket price=",amount)
        else:
            amount=price*(125/100)
            print("ticket price=",amount)
    if show=="afternoon show":
          if age<=5:
            amount=price*(50/100)*(125/100)*(110/100)
            print("ticket price=",amount)
          elif age>=60:
            amount=price*(90/100)*(125/100)*(110/100)
            print("ticket price=",amount)
          else:
            amount=price*(125/100)*(110/100)
            print("ticket price=",amount)
    if show=="evening show":
             if age<=5:
                 amount=price*(50/100)*(125/100)*(130/100)
                 print("ticket price=",amount)
             elif age>=60:
                 amount=price*(90/100)*(125/100)*(130/100)
                 print("ticket price=",amount)
             else:
                 amount=price*(125/100)*(130/100)
                 print("ticket price=",amount)
if day=="weekday":
    if show=="morning show":
        if age<=5:
          amount=price*(50/100)
          print("ticket price=",amount)
        elif age>=60:
          amount=price*(90/100)
          print("ticket price=",amount)
        else:
          amount=price
          print("ticket price=",amount)
    if show=="afternoon show":
         if age<=5:
            amount=price*(50/100)*(110/100)
            print("ticket price=",amount)
         elif age>=60:
            amount=price*(90/100)*(110/100)
            print("ticket price=",amount)
         else:
             amount=price*(110/100)
             print("ticket price=",amount)
    if show=="evening show":
          if age<=5:
               amount=price*(50/100)*(130/100)
               print("ticket price=",amount)
          elif age>=60:
               amount=price*(90/100)*(130/100)
               print("ticket price=",amount)
          else:
               amount=price*(130/100)
               print("ticket price=",amount)

                    