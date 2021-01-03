rollno=input("Enter roll no:")
name=input("Enter name:")
sub1=int(input("Enter sub1:"))
sub2=int(input("Enter sub2:"))
sub3=int(input("Enter sub3:"))
sub4=int(input("Enter sub4:"))
sub5=int(input("Enter sub5:"))
sub6=int(input("Enter sub6:"))
totalmarks=sub1+sub2+sub3+sub4+sub5+sub6
sub=[sub1,sub2,sub3,sub4,sub5,sub6]
for x in sub:
    print("Passed") if x >= 40 else print("Promoted")
avg=(totalmarks/6)
if avg >=80:
    grade="A"
elif 79>=avg>=60:
    grade="B"
elif 59>=avg>=50:
    grade="B"
elif 49>=avg>=40:
    grade="B"
else:
     grade="Promoted"            
print("Rollno",rollno)
print("Name",name)
print("totalmarks",totalmarks)
print("Average",avg)
print("grade",grade)


