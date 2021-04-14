import mysql.connector

from mysql.connector import Error

class DBConnector:

    cursor,connection = None,None

    #Start DB Connection
    def __init__(self):
        
        try:
            self.connection = mysql.connector.connect(host='localhost', database='office', user='root', password='123456789')

            self.cursor = self.connection.cursor()

        except Error as e:
            
            print("Error: ", e)


    #Get All Employee
    def selectAll(self):
    
        self.cursor.execute("""
                            SELECT * FROM employees
                            """)
        
        print(self.cursor.fetchall())

        self.connection.close()
    

    #Get one Employee
    def selectOne(self, empID):

        self.cursor.execute("""
                            SELECT * FROM employees WHERE id = %s
                            """,(empID, ))

        print(self.cursor.fetchall())

        self.connection.close()


    #Get All Managers                        
    def selectManagers(self):

        self.cursor.execute("""
                            SELECT id, username FROM employees WHERE is_manager = 1
                            """)

        print(self.cursor.fetchall())

        self.connection.close()


    #Insert Employee
    def insert(self, id, username, work_hours, salary):

        self.cursor.execute("""
                            INSERT INTO employees (id, username, work_hours, salary) VALUES (%s, %s, %s, %s)
                            """, (id, username, work_hours, salary))

        self.connection.commit()

        self.connection.close()


    #Promote Employee
    def upgrade(self, empID):

        self.cursor.execute("""
                            UPDATE employees set is_manager = 1 WHERE id = %s
                            """, (empID, ))

        self.connection.commit()

        self.connection.close()

        print("Employee is Hired!!!")


    #Delete Employee
    def delete(self, empID):
        
        self.cursor.execute("""
                            DELETE FROM employees WHERE id = %s
                            """, (empID, ))

        self.connection.commit()

        self.connection.close()

        print("Employee is Fired!!!")


    #Deduct the Money
    def deduct(self, empID, deductMoney):

        self.cursor.execute("""
                            UPDATE employees SET money = money - %s WHERE id = %s
                            """, (deductMoney, empID))

        self.connection.commit()

        self.connection.close()

        print("Deduction Created Successfully!!!")
    

    #Add Meal
    def addMeal(self, meals_no, healthRate, empID):

        self.cursor.execute("""
                            UPDATE employees SET meal = %s AND healthRate = %s WHERE id = %s
                            """, (meals_no, healthRate, empID))

        self.connection.commit()

        self.connection.close()

        print("Meals Added Successfully!!!")


    #Sleep Rate
    def sleepRate(self, hours, sleepmood, empID):

        self.cursor.execute("""
                            UPDATE employees SET sleep_hours = %s AND sleepmood = %s WHERE id = %s
                            """, (hours, sleepmood, empID))

        self.connection.commit()

        self.connection.close()

        print("SleepRate Added Successfully!!!")


    #Get Meal Number
    def getMealNumber(self, empID):

        self.cursor.execute("""
                            SELECT meals_no FROM employees WHERE id = %s
                            """, (empID, ))

        meals_no = self.cursor.fetchall()

        self.connection.close()

        return meals_no


    #Get Work Hours
    def getWorkHours(self, empID):

        self.cursor.execute("""
                            SELECT work_hours FROM employees WHERE id = %s
                            """, (empID, ))

        work_hours = self.cursor.fetchall()

        self.connection.close()

        return work_hours


    #Update Work Hours
    def updateWorkHours(self, hours, workMood,empID):

        self.cursor.execute("""
                            UPDATE employees SET work_hours = %s AND workmood = %s WHERE id = %s
                            """, (hours, workMood, empID))

        self.connection.commit()

        self.connection.close()

        print("Work Hours Updated Successfully!!!")