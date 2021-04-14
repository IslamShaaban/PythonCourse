from DBOps import DBConnector

class Person:

    _connector, _full_name, _money, _sleepMood, _healthRate = None, None, None, None, None


    def __init__(self):

        self.connector = DBConnector

    
    def setName(self):

        self._full_name = input("Enter Employee Name: ")


    def getName(self):

        return self._full_name

    
    #Sleep Mood of Employee in Office
    def sleep(self, hours):
        pass


    #Health Rate of Employee in Office    
    def eat(self, meals_no):
        pass


    #Total Money of Employee
    def buy(self, items):
        pass