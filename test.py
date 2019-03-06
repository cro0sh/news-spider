import csv

interest = ['Trump', ]

with open("goognews.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        for something in row:
            for z in interest:
                if z in something:
                    print(something)
##        print(row)
