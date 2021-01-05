list=[]
while True:
    print("My To Do App")
    print("============")
    print("1.Add Task")
    print("2.View all Task")
    print("0.Exit")
    option=input("Select option")
    if option=="1":
        i1 = input("Enter task name:")
        list.append(i1)
        print("Task Added")
    elif option=="2":
        print(list)
    else:
        print("Bye")
        break
