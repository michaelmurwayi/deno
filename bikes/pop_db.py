import sys
import os
import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="huncho",
  passwd="c11h28no3",
  database="bikes"

)

def read_csvfile_to_list(uploaded_file):
    # read packages records from csv records
    with open(uploaded_file, newline='') as csvfile:
        Line_count = 0
        package_list = []
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
        for row in spamreader:
            # import ipdb; ipdb.set_trace()
            # if Line_count == 0:
            #     Line_count += 1
            #     column_name = row
            #     import ipdb; ipdb.set_trace()
            # else:
            #     Line_count += 1
            package_list.append(row)

    return package_list


def push_to_db(package_list):
    # pushing csv list records into db

    for lists in package_list:
        for items in lists:
            # import ipdb; ipdb.set_trace()
            sql = "INSERT INTO bikes_bike (id, station_id, working, rental_id) VALUES ( %d )"
            cursor = mydb.cursor()
            cursor.execute(sql, items)
            mydb.commit()
            print(cursor.rowcount,
                "Record inserted successfully into packges database")
            cursor.close()

    return "records inserted"


if __name__ == '__main__':
    uploaded_file = input("Enter File Name: ")
    list_of_packages = read_csvfile_to_list(uploaded_file)
    push_to_db(list_of_packages)
