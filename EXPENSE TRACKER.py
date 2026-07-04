file = "expenses.txt"

def add_expense():
    try:
        cat = input("Category: ")
        amt = float(input("Amount: "))

        with open(file, "a") as f:
            f.write(cat + "," + str(amt) + "\n")

        print("Saved")
    except ValueError:
        print("Invalid amount")

def show_summary():
    try:
        data = {}

        with open(file, "r") as f:
            for line in f:
                cat, amt = line.strip().split(",")
                amt = float(amt)

                if cat in data:
                    data[cat] += amt
                else:
                    data[cat] = amt

        for k, v in data.items():
            print(k, ":", v)

    except FileNotFoundError:
        print("No records")

    except ValueError:
        print("Corrupted file")

while True:
    c = input("\n1.Add 2.Summary 3.Exit: ")

    if c == "1":
        add_expense()
    elif c == "2":
        show_summary()
    elif c == "3":
        break
    else:
        print("Invalid choice")