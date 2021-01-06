def max_element_list(list):
    list.sort()
    return print(list[-1])

list=[2,3,4,5,3,10,3,6]
max_element_list(list)

def min_element_tuple(tuple):
    sorted(tuple)
    return print(list[0])

tuple=(11,2,3,4,5,3,10,3,6)
min_element_tuple(tuple)

fact=1
def factorial(num):
    fact=1
    for x in range(1,num+1):
        fact=fact*x
    print(fact)

factorial(5)

def my_reverse(name):
    return print(name[::-1])

my_reverse("pushkar")
