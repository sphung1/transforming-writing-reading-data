import csv




#Get the data and remove the gender and title
    #return transformed data
def transform_user_details(csv_full_name):
    new_user_data = []

    with open('user_details.csv', newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=',')

        for row_list in user_details_csv:
            transformed_row = []
            transformed_row.append(row_list[1].capitalize())
            #print (row_list[1])
            transformed_row.append(row_list[2].capitalize())
            #print (row_list[2])
            transformed_row.append(row_list[4])
            #print (row_list[4]
            #here we can strip concatanante and capitalise
            new_user_data.append(transformed_row)
    return new_user_data

print(transform_user_details('user_details.csv'))
trasnf_data = transform_user_details('user_details.csv')

#lets create a function to write our transformed data
    #write to csv

def create_new_csv_user_data (transformed_data, new_user_file_name):

    #have our transformed data
    #open a new file
    #use option to write
    new_file = open(new_user_file_name, 'w', newline='')


    # write to that file
    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows (transformed_data)
    


create_new_csv_user_data(trasnf_data, 'transformed_csv.csv')








