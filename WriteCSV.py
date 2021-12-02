import csv

with open('mycsv.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['col1', 'col2', 'col3'])
    for i in range(1, 100):
        thewriter.writerow(['one', 'four', '8'])
