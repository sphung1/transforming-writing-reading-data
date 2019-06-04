import csv
# HERE we load the csv
    #open the file
    #read line by line
    #separate in commas

# with open('user_details.csv', newline='') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter = ',')
#     print(csvreader)
#     for row in csvreader:
#         print(row[-1])
#       #  print(type(row))

with open('user_details.csv', newline='') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
    list_list = list(csvreader)
   # print(list_list)
    print(type(list_list))
    print(len(list_list))
    for list in (list_list):
        print(list)

#Transforming and writing to CSV






# iter() to skip over the first line
#iter () to make iteratable object
#next () to go to the next line
# with open('user_details.csv', newline='') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter = ',')
#
#     iteratable = iter(csvreader)
#     print(iteratable)
#     #print(type(next(iteratable)))
#     headers = next(iteratable)
#     for row in iteratable:
#         print(row)