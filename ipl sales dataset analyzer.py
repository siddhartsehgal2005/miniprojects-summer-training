import csv
sales = []

with open("ipl_sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        sales.append(int(row[1]))

print("Total Sales:", sum(sales))
print("Highest Sales:", max(sales))
print("Lowest Sales:", min(sales))