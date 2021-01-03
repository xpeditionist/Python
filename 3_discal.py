dis=0
totalamt=0
while True:
    
    amt=int(input("Please Enter Purchase amount:"))
    if 100>=amt>=1000 :
        dis=0
        totalamt=amt
    elif 1001<=amt<=2000 :
        dis=0.1*amt
        totalamt=amt-dis
    elif 2001<=amt<=3000 :
        dis=0.2*amt
        totalamt=amt-dis
    elif 2001<=amt<=3000 :
        dis=0.25*amt
        totalamt=amt-dis
    elif 3001<=amt :
        dis=0.25*amt
        totalamt=amt-dis
    else:
        print("Discount Not Applicable")
    
    print("Purchase amount",amt)
    print("Discount",dis)
    print("Total Amount",totalamt)
    x=input("Do U want to continue (yes or no)")
    if x != 'yes':
        print("bye")
        break
    
        

