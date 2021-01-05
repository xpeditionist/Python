string="PYThon"
list1=[]
for x in string:
    list1.append(x)
list=["P","Y","T","H","O","N"]
list2=[ i for i in list1 if i in list]
for x in list2:
    print(x)