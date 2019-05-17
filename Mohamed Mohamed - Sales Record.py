import csv


print("Procesing...")
with open("Sales.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        Fruits = 0
        Clothes = 0
        Meat = 0
        Beverages = 0
        Office_Supplies = 0
        Cosmetics = 0
        Personal_Care = 0
        Household = 0
        Baby_Food = 0
        Vegetables = 0
        Snacks = 0
        Cereal = 0
        item_list = []
        for row in reader:
            item_type = row[2]
            if row[2] == "Fruits":
                profit = float(row[13])
                for i in row[13]:
                    Fruits += profit
            elif row[2] == "Clothes":
                profit = float(row[13])
                for i in row[13]:
                    Clothes += profit
            elif row[2] == "Beverages":
                profit = float(row[13])
                for i in row[13]:
                    Beverages += profit
            elif row[2] == "Meat":
                profit = float(row[13])
                for i in row[13]:
                    Meat += profit
            elif row[2] == "Office Supplies":
                profit = float(row[13])
                for i in row[13]:
                    Office_Supplies += profit
            elif row[2] == "Cosmetics":
                profit = float(row[13])
                for i in row[13]:
                    Cosmetics += profit
            elif row[2] == "Personal Care":
                profit = float(row[13])
                for i in row[13]:
                    Personal_Care += profit
            elif row[2] == "Household":
                profit = float(row[13])
                for i in row[13]:
                    Household += profit
            elif row[2] == "Baby Food":
                profit = float(row[13])
                for i in row[13]:
                    Baby_Food += profit
            elif row[2] == "Vegetables":
                profit = float(row[13])
                for i in row[13]:
                    Vegetables += profit
            elif row[2] == "Snacks":
                profit = float(row[13])
                for i in row[13]:
                    Snacks += profit
            elif row[2] == "Cereal":
                profit = float(row[13])
                for i in row[13]:
                    Cereal += profit


print("The Fruit profit is %d" % Fruits)
print("The Clothes profit is %d" % Clothes)
print("The Meat profit is %d" % Meat)
print("The Beverages profit is %d" % Beverages)
print("The Office Supplies profit is %d" % Office_Supplies)
print("The Cosmetics profit is %d" % Cosmetics)
print("The Personal Care profit is %d" % Personal_Care)
print("The Household profit is %d" % Household)
print("The Baby_Food profit is %d" % Baby_Food)
print("The Vegetables profit is %d" % Vegetables)
print("The Snacks profit is %d" % Snacks)
print("The Cereal profit is %d" % Cereal)

profit = [Fruits, Clothes, Meat, Beverages, Office_Supplies, Cosmetics, Personal_Care, Household, Baby_Food, Vegetables,
          Snacks, Cereal]


if max(profit) == Fruits:
    print("The most profitable are Fruit")
if max(profit) == Clothes:
    print("The most profitable are Clothes")
if max(profit) == Meat:
    print("The most profitable are Meat")
if max(profit) == Beverages:
    print("The most profitable are Beverages")
if max(profit) == Office_Supplies:
    print("The most profitable are Office Supplies")
if max(profit) == Cosmetics:
    print("The most profitable are Cosmetics")
if max(profit) == Personal_Care:
    print("The most profitable are Personal Care")
if max(profit) == Household:
    print("The most profitable are Household")
if max(profit) == Baby_Food:
    print("The most profitable are Baby Food")
if max(profit) == Vegetables:
    print("The most profitable are Vegetables")
if max(profit) == Snacks:
    print("The most profitable are Snacks")
if max(profit) == Cereal:
    print("The most profitable are Cereal")









