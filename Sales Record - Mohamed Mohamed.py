import csv


with open("Sales.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        totalA = 0
        totalB = 0
        totalC = 0
        totalD = 0
        totalE = 0
        totalF = 0
        totalG = 0
        totalH = 0
        totalI = 0
        TotalJ = 0
        totalK = 0
        totalL = 0
        item_list = []
        for row in reader:
            if row[0] == "Region":
                continue
                item_type = row[2]
                if row[2] == "Fruits":
                    total += float(row[13])
                if row[2] == "Clothes":
                    total += float(row[13])
                print(total)
                print(item_list)