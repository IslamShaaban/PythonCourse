###Implementing The Menu Interface of Program
from OfficeController import Office

from EmployeeController import Employee


office = Office()

employee = Employee()
def showMenu():
    
    flag = True
    
    while flag:
        print("Welcome to Our Program")
        print("Select one of The Option below to Implement Your Required By Choose Number")
        print("1) Show All Employees")
        print("2) Show Employee Info")
        print("3) Show All Managers")
        print("4) Promote An Employee")
        print("5) Add An Employee")
        print("6) Delete An Employee")
        print("7) Add Meal to An Employee")
        print("8  Add Sleep Hours of Employee")
        print("9) Update Work Hours of Employee")
        print("10) Exit")

        choice = int(input('Enter Your Choice: '))
        
        def Choice(choice):
            if choice == 1:
                office.get_all_employees()
            elif choice == 2:
                office.get_employee()
            elif choice == 3:
                office.get_managers()
            elif choice == 4:
                office.promote()
            elif choice == 5:
                office.hire()
            elif choice == 6:
                office.fire()
            elif choice == 7:
                meals_no = input("Enter Meals No: ")
                employee.eat(meals_no)
            elif choice == 8:
                hours = input("Enter Hours: ")
                employee.sleep(hours)
            elif choice == 9:
                hours = input("Enter Hours: ")
                employee.work(hours)
        Choice(choice)
        if choice == 10:
            flag = False
showMenu()