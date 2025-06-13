#  File: EmployeeSalaries.py
#  Student Name: SaiSathvik Katta
#  Student UT EID: sk49699

class Employee:
    def __init__(self, **kwargs):
        pass
        """
        This function uses kwargs to initialize the name, id, and the salary variables of the Employee class.
        """
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary')
        if self.salary == None:
            #Sets base salary
            self.salary = 80000

    def get_salary(self):
        pass
        """
        This function calculates the salary of the Employee and returns it as a float.
        """
        return float(self.salary)

    def __str__(self):
        pass
        """
        This function uses f-strings and returns relevant information about the Employee.
        """
        return (f'Employee\n{self.name},{self.id},{self.salary}')

########################################################################################################################
class Permanent_Employee(Employee):
    def __init__(self, **kwargs):
        pass
        """
        This function uses kwargs to initialize the name, id, salary and the benefit variables of the 
        Permanent Employee class using the Employee superclass.
        """
        Employee.__init__(self, **kwargs)
        self.benefits = kwargs.get('benefits', [])
        #Sets the base salary
        self.base_salary = self.salary
        #Creates two boolean variables to determine what type of benefit the Permanent Employee should receive.
        self.health_insurance = False
        self.retirement_insurance = False
    def cal_salary(self):
        pass
        """
        This function calculates the salary of the Permanent Employee and returns it as a float.
        """
        if self.benefits == None:
            pass
        else:
            #Determines what benefits the employee receives.
            for i in self.benefits:
                if i == 'health_insurance':
                    self.health_insurance = True
                else:
                    self.retirement_insurance = True

        #Calucutes the employees salary based on the benefits they receive.
        if self.health_insurance == True and self.retirement_insurance == False:
            self.salary = float(self.base_salary)*0.9
            return float(self.salary)
        elif self.health_insurance == False and self.retirement_insurance == True:
            self.salary = float(self.base_salary)*0.8
            return float(self.salary)
        elif self.health_insurance == True and self.retirement_insurance == True:
            self.salary = float(self.base_salary)*0.7
            return float(self.salary)
        else:
            pass
        return float(self.salary)

    def __str__(self):
        pass
        """
        This function uses f-strings and returns relevant information about the Permanent Employee.
        """
        return (f'Permanent_Employee\n{self.name},{self.id},{self.salary},{self.benefits}')

########################################################################################################################
class Manager(Employee):
    def __init__(self, **kwargs):
        pass
        """
        This function uses kwargs to initialize the name, id, salary and bonus variables of the Manager class using the
        Employee superclass.
        """
        Employee.__init__(self, **kwargs)
        self.bonus = kwargs.get('bonus')
    def cal_salary(self):
        pass
        """
        This function calculates the salary of the Manager and returns it as a float.
        """
        self.salary = float(self.salary) + self.bonus
        return float(self.salary)

    def __str__(self):
        pass
        """
        This function uses f-strings and returns relevant information about the Manager.
        """
        return (f'Manager\n{self.name},{self.id},{self.salary},{self.bonus}')

########################################################################################################################
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        pass
        """
        This function uses kwargs to initialize the name, id, salary and hours variables of the Temporary Employee class
        using the Employee superclass.
        """
        Employee.__init__(self, **kwargs)
        self.hours = kwargs.get('hours')
    def cal_salary(self):
        pass
        """
        This function calculates the salary of the Temporary Employee and returns it as a float.
        """
        self.salary = self.salary*self.hours
        return float(self.salary)

    def __str__(self):
        pass
        """
        This function uses f-strings and returns relevant information about the Temporary Employee.
        """
        return (f'Temporary_Employee\n{self.name},{self.id},{self.salary},{self.hours}')

########################################################################################################################
class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        pass
        """
        This function uses kwargs to initialize the name, id, salary, hours and travel variables of the 
        Consultant class using the Temporary Employee superclass.
        """
        Temporary_Employee.__init__(self, **kwargs)
        self.travel = kwargs.get('travel')
    def cal_salary(self):
        pass
        """
        This function calculates the salary of the Consultant and returns it as a float.
        """
        self.salary = (self.salary*self.hours)+(self.travel*1000)
        return float(self.salary)

    def __str__(self):
        pass
        """
        This function uses f-strings and returns relevant information about the Consultant.
        """
        return (f'Consultant\n{self.name},{self.id},{self.salary},{self.hours},{self.travel}')

########################################################################################################################
class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs):
        pass
        """
        This function uses kwargs to initialize the name, id, salary, hours, travel and bonus variables of the 
        Consultant_Manager class using the Consultant and Manager superclasses.
        """
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)
    def cal_salary(self):
        pass
        """
        This function calculates the salary of the Consultant_Manager and returns it as a float.
        """
        self.salary = (self.salary*self.hours)+(self.travel*1000)+self.bonus
        return float(self.salary)

    def __str__(self):
        pass
        """
        This function uses f-strings and returns relevant information about the Consultant_Manager.
        """
        return (f'Consultant_Manager\n{self.name},{self.id},{self.hours},{self.travel},Consultant_Manager\n'
                f'{self.name},{self.id},{self.salary},{self.bonus}')

########################################################################################################################

def calculate_total_salaries(employee_list):
    pass
    """
    This function takes a list of employees and calculates their total salary.
    
    :return: Returns the total salary of all the employees.
    """
    total_salaries = 0
    for employee in employee_list:
        total_salaries += employee.salary
    return total_salaries

def calculate_manager_salaries(employee_list):
    pass
    """
    This function take a list of employees and calculates the salary of only the managers.

    :return: Returns the total salary of only the managers.
    """
    manager_salaries = 0
    for employee in employee_list:
        #Uses isinstance to calculate the salaries of only the Consultant_Manager and Manager classes
        if isinstance(employee, Consultant_Manager) or isinstance(employee, Manager):
            manager_salaries += employee.salary

########################################################################################################################
''' ##### DRIVER CODE #####
    ##### Do not change. '''

# create employees
chris = Employee(name="Chris", id="UT1")
emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)

# print employees
print(chris, "\n")
print(emma, "\n")
print(sam, "\n")
print(john, "\n")
print(charlotte, "\n")
print(matt, "\n")

# calculate and print salaries
print("Check Salaries")
print("Emma's Salary is:", emma.cal_salary())
emma.benefits = ["health_insurance"]
print("Emma's Salary is:", emma.cal_salary())
emma.benefits = ["retirement", "health_insurance"]
print("Emma's Salary is:", emma.cal_salary())
print("Sam's Salary is:", sam.cal_salary())
print("John's Salary is:", john.cal_salary())
print("Charlotte's Salary is:", charlotte.cal_salary())
print("Matt's Salary is:",  matt.cal_salary())

