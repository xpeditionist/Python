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
        num1=int(input("Enter Number:"))
        num2=int(input("Enter Number:"))
        sum = num1+num2;
        print("Result: ",sum)
    elif option==2 :
        num1=int(input("Enter Number:"))
        num2=int(input("Enter Number:"))
        sub = num1-num2;
        print("Result: ",sub)
    elif option==3 :
        num1=int(input("Enter Number:"))
        num2=int(input("Enter Number:"))
        multi = num1*num2;
        print("Result: ",multi)
    elif option==4 :
        num1=int(input("Enter Number:"))
        num2=int(input("Enter Number:"))
        div = num1/num2;
        print("Result: ",div)
    elif option==0:
        print("bye")
        break
    
    else:
        print("Please choose correct option")
    
    x=input("Do U want to continue (yes or no)")
    if x != 'yes':
        print("bye")
        break
    

