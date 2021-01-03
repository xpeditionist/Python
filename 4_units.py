rate=0
billamt=0
while True:
    
    units=int(input("Please Enter Units:"))
    if 1<=units<=50 :
        rate=3
        billamt=rate*units
    elif 51<=units<=100 :
        rate=6
        billamt=rate*units
    elif 101<=units<=150 :
        rate=9
        billamt=rate*units
    elif 151<=units<=200 :
        rate=12
        billamt=rate*units
    elif 201<=units :
        rate=15
        billamt=rate*units
     
    print("Units",units)
    print("Bill Amount",billamt)
    x=input("Do U want to continue (yes or no)")
    if x != 'yes':
        print("bye")
        break
