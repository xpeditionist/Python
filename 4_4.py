dict1={}
while True:
    print("My To Do App")
    print("============")
    print("1.Add Task")
    print("2.View all Task")
    print("0.Exit")
    option=input("Select option")
    if option=="1":
        i1 = input("Enter task name:")
        i2 = input("Enter date: ")
        dict1[i1]=i2
        print("Task Added")
    elif option=="2":
        print(dict1)
    else:
        print("Bye")
        break

