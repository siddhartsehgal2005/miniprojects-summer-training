class Error(Exception):
    pass
class Employee:
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def calc(self):
        if self.sal < 0:
            raise Error("Invalid salary")

        a = self.sal * 0.2
        d = self.sal * 0.1
        f = self.sal + a - d
        return a, d, f
ids = []
emps = {}

n = int(input("No of employees: "))

for i in range(n):
    try:
        eid = input("ID: ")
        name = input("Name: ")
        sal = float(input("Salary: "))

        e = Employee(eid, name, sal)
        ids.append(eid)
        emps[eid] = e

    except:
        print("Invalid input")

print("\nReport")

for i in ids:
    try:
        a, d, f = emps[i].calc()
        print(i, emps[i].name, f)
    except:
        print(i, "Error")