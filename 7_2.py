while True:
    print("My To Do App")
    print("============")
    print("1.Add Task")
    print("2.View all Task")
    print("0.Exit")
    option=input("Select option")
    if option=="1":
        i1 = input("Enter task name:")
        f=open("file2.txt",'w')
        f.write(i1)
        f.close()
        print("Task Added")
    elif option=="2":
        f=open("file2.txt",'r')
        data=f.read()
        print(data)
        f.close()
    else:
        print("Bye")
        break

