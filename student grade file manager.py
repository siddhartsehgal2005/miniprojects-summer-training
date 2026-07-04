import csv

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

input_file = "students.csv"
output_file = "students_updated.csv"

try:
    with open(input_file, "r") as f:
        reader = csv.reader(f)
        next(reader)

        with open(output_file, "w", newline="") as out:
            writer = csv.writer(out)
            writer.writerow(["Name", "Marks", "Grade"])

            for row in reader:
                name = row[0]
                marks = int(row[1])
                grade = get_grade(marks)

                writer.writerow([name, marks, grade])

    print("Updated file created:", output_file)

except FileNotFoundError:
    print("Input file not found")

except ValueError:
    print("Invalid data in file")