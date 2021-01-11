class AttendanceShortageException(Exception):
    def __init__(self,arg):
        self.msg=arg

class IncomeException(Exception):
    def __init__(self,arg):
        self.msg=arg

class GPAException(Exception):
    def __init__(self,arg):
        self.msg=arg

att=int(input("Enter Student Attendance:"))
income=int(input("Enter Student's parents Income:"))
GPA=int(input("Enter Student GPA:"))

if att<75:
    raise AttendanceShortageException("More attendance required.")
elif income>500000:
    raise IncomeException("Not eligible as income is higher")
elif GPA<7:
    raise GPAException("GPA required more than 7")
else:
    print("Student is elibigle for addmission.")
    
