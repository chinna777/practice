from abc import abstractmethod,ABC
class EmployeePayRole(ABC):
    def __init__(self,empid,empname):
        self.empid=empid
        self.empname=empname
       # self.emprole=emprole
    @abstractmethod
    def empCal(self):
        pass
class Admin(EmployeePayRole) :
    super().empCal(emprole)
    print("hey your salary calculated check out for newupdates")

class Clerk(EmployeePayRole):
    super().empCal(emprole)
    print("hey clerk you didnt got salary yet")




       
