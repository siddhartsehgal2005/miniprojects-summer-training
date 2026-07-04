import csv

file = "books.csv"

def add():
    b = input("Book: ")
    with open(file, "a", newline="") as f:
        csv.writer(f).writerow([b])
    print("Added")

def view():
    try:
        with open(file, "r") as f:
            for r in csv.reader(f):
                print("-", r[0])
    except FileNotFoundError:
        print("No file")

def search():
    try:
        b = input("Search: ")
        with open(file, "r") as f:
            for r in csv.reader(f):
                if r[0] == b:
                    print("Found")
                    return
        print("Not found")
    except FileNotFoundError:
        print("No file")

def remove():
    try:
        b = input("Remove: ")
        data = []
        with open(file, "r") as f:
            for r in csv.reader(f):
                if r[0] != b:
                    data.append(r)
        with open(file, "w", newline="") as f:
            csv.writer(f).writerows(data)
        print("Done")
    except FileNotFoundError:
        print("No file")

while True:
    c = input("\n1.Add 2.View 3.Search 4.Remove 5.Exit: ")
    if c == "1": add()
    elif c == "2": view()
    elif c == "3": search()
    elif c == "4": remove()
    elif c == "5": break
    else: print("Invalid")