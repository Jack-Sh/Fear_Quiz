import csv 

file = open("fear_list.csv", "r")
all_fears = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row (header values)
all_fears.pop(0)

# get the first 50 rows (used to develop colour buttons for play GUI)
print(all_fears[:50])

print("Length: {}".format(len(all_fears)))