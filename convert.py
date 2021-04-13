import csv

with open('logs.csv', newline='') as logs:
  csv_data = csv.DictReader(logs)

  i = 0
  for row in csv_data:
    # only prints 10 first rows
    if i < 10:
      print(row)
    
    i += 1
  
print("Done in xxx seconds")