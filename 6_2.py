def print_table(num):
    for x in range(1,11):
        print(x*num)

print_table(10)

def max(num1,num2):
    print(num1) if num1>num2 else print(num2)

max(4,5)

def max(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1)
    elif num2>num1 and num2>num3:
        print(num2)
    else:
        print(num3)
max(2,6,4)            




