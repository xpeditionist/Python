while True:
    print("MY CALC APP")
    print("===========")
    print("1. To add")
    print("2. To sub")
    print("3. To multi")
    print("4. To div")
    print("0. To Exit")

    option=int(input("Please Choose Options:"))
    if option==1 :
        try:
            num1=int(input("Enter Number:"))
            num2=int(input("Enter Number:"))
            sum = num1+num2;
            print("Result: ",sum)
        except ValueError:
            print('Please Enter only number')
    elif option==2 :
        try:
            num1=int(input("Enter Number:"))
            num2=int(input("Enter Number:"))
            sub = num1-num2;
            print("Result: ",sub)
        except ValueError:
            print('Please Enter only number')
    elif option==3 :
        try:
            num1=int(input("Enter Number:"))
            num2=int(input("Enter Number:"))
            multi = num1*num2;
            print("Result: ",multi)
        except ValueError:
            print('Please Enter only number')
    elif option==4 :
        try:
            num1=int(input("Enter Number:"))
            num2=int(input("Enter Number:"))
            div = num1/num2;
            print("Result: ",div)
        except ValueError:
            print('Please Enter only number')
        except ZeroDivisionError:
            print("Can't divide a number by 0")
       
    elif option==0:
        print("bye")
        break
    
    else:
        print("Please choose correct option")
    
    x=input("Do U want to continue (yes or no)")
    if x != 'yes':
        print("bye")
        break
    

