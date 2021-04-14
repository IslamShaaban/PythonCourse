from DBOps import DBConnector

from PersonController import Person

class Employee(Person):

    connector, _workMood, _salary, _isManager, _id, _email = None, None, None, None, None, None


    def __init__(self):

        self.connector = DBConnector()
    
    #Measure Work Rate
    def work(self, hours):

        self._id = int(input("Enter Employee ID: "))

        hours += self._connector.getWorkHours(self._id)

        if hours > 8:
            self._workMood = 'happy'

        elif hours < 8:
            self._workMood = 'lazy'
            
        else:
            self._workMood = 'tired'

        self._connector.addMeal(hours, self._workMood, self._id)


    #Send Email to Person
    def sendEmail(self, to, subject, bodyReciever):
        
        f = open('email.txt', 'w')
        self._email = f'to : {to} \n' \
                      f'subject : welcome email \n' \
                      f'reciever : {bodyReciever} \n' \
                      f'welcome to Our Project'
        f.write(self._email)
        f.close()    


    #Deduction Money of Employee
    def buy(self, items):

        self._id = int(input("Enter Employee ID: "))

        self._money = self._money - (items * 10)

        self._connector.deduct(self._id, self._money)


    #Sleep Rate of Employee
    def sleep(self, hours):
        
        self._id = int(input("Enter Employee ID: "))
        
        if hours > 7:
            self._sleepMood = 'lazy'

        elif hours < 7:
            self._sleepMood = 'tired'
            
        else:
            self._sleepMood = 'happy'

        self._connector.sleepRate(hours, self._sleepMood, self._id)


    #Health Rate of Employee
    def eat(self, meals_no):
        
        self._id = int(input("Enter Employee ID: "))

        meals_no += self._connector.getMealNumber(self._id)

        if meals_no >= 3:
            self._healthRate = 100
        
        elif meals_no == 2:
            self._healthRate = 75

        elif meals_no == 1:
            self._healthRate = 50

        self._connector.addMeal(meals_no, self._healthRate, self._id)