import csv
import tkinter as tk
from tkinter import filedialog
from collections import defaultdict

def main():
    print("Hello World!")
    root = tk.Tk()
    w = tk.Label(text="Hello, Tkinter")
    w.pack()
    btn = tk.Button(
            text="Select CSV",
            width=25,
            height=5,
            command=getCSVPress,
            )
    btn.pack()
    root.mainloop()

def getCSVPress():
    palletDict = defaultdict(list)
    filepath = filedialog.askopenfilename()
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            item_num = row[0]
            location = row[1]
            qty = row[2]
            for loc in location.split(','):
                loc = loc.rstrip('0')
                if len(loc) < 3:
                    continue
                l = loc[0]
                n = loc[1:-1]
                s = loc[-1]
                palletDict[(l,n,s)].append((item_num, qty))

    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    numbers = [str(n) for n in numbers]
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    shelves = ['H','M','S','F']
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for l in letters:
            writer.writerows([[]])
            writer.writerows([[l] + numbers])
            writer.writerows([[]])
            for s in shelves:
                for row in getRows(palletDict, l, s, numbers):
                    writer.writerows([[s]+row])



def getRows(palletDict, l, s, numbers):
    rows = []
    numrows = max([len(palletDict[(l,n,s)]) for n in numbers])
    for r in range(numrows):
        newrow = []
        for n in numbers:
            if len(palletDict[(l,n,s)]) >= r+1:
                item_num, qty = palletDict[(l,n,s)][r]
                newrow.append(item_num+'('+qty+')')
            else:
                newrow.append('')
        rows.append(newrow)
    return rows

if __name__ == "__main__":
    main()
