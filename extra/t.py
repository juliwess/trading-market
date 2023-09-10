import csv

if __name__ == '__main__':
    with open('GUI/values.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(row[0])