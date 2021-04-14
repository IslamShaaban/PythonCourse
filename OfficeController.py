from DBOps import DBConnector

from EmployeeController import Employee

class Office:

    connector, empID = None, None

    def __init__(self):

        self.connector = DBConnector()

    #Get All Employees
    def get_all_employees(self):

        self.connector.selectAll()


    #Get Certain Employee    
    def get_employee(self):

        self.empID = int(input("Enter Employee ID: "))

        self.connector.selectOne(self.empID)


    #Get All Managers
    def get_managers(self):

        self.connector.selectManagers()


    #Upgrade Employee    
    def promote(self):

        self.empID = int(input("Enter Employee ID: "))

        self.connector.upgrade(self.empID)
        

    #Hire New Employee
    def hire(self):

        id = input('id: ')
        name = input('name : ')
        salary = input('salary : ')
        work_hours = input('work hours: ')
        self.connector.insert(id, name, salary, work_hours)
        
        
    #Delete Employee
    def fire(self):

        self.empID = int(input("Enter Employee ID: "))

        self.connector.delete(self.empID)