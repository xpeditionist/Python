sum=0
def func(num):
    sum=0
    num1=str(num)
    for x in range(0,len(num1)):
        sum=sum+int((num1[x]))
    print(sum)
    print(num1[::-1])
func(1234)