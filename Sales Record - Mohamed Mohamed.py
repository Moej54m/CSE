import csv


with open("Sales.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            if row[2] == "Fruits":
                print(row[2])
                print(row[13]