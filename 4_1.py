list=[10,10,20,20,30]
for x in list:
    s=list.count(x)
    print(s)
    if s>1:
        list.remove(x)
print(list)        
            