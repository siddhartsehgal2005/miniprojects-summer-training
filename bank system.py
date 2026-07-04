class Error(Exception):
    pass

class Account:
    def __init__(self, a, n, b):
        self.a = a
        self.n = n
        self.b = b

    def deposit(self, x):
        self.b += x
        self.log("Deposit", x)

    def withdraw(self, x):
        if x > self.b:
            raise Error("Insufficient balance")
        self.b -= x
        self.log("Withdraw", x)

    def balance(self):
        return self.b

    def log(self, t, x):
        with open("txn.txt", "a") as f:
            f.write(f"{self.a},{t},{x},{self.b}\n")
acc = {}
lst = []

n = int(input("Customers: "))

for i in range(n):
    a = input("Acc No: ")
    n1 = input("Name: ")
    b = float(input("Balance: "))
    acc[a] = Account(a, n1, b)
    lst.append(a)

c = input("1.Dep 2.Wit 3.Bal: ")
a = input("Acc No: ")

try:
    if c == "1":
        acc[a].deposit(float(input("Amt: ")))
    elif c == "2":
        acc[a].withdraw(float(input("Amt: ")))
    else:
        print(acc[a].balance())
except:
    print("Error")