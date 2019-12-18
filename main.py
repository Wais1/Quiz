import csv

class Staff:
    __id_list = []

    def display_menu(self):
        response = -1
        while response < 1 or response > 4:
            response = int(input("1. New Staff\n2. Delete Staff\n3. View Summary Data\n4. Save and Exit"))
        return response

    def test(self):
        numbers = ["0,1,2,3,4,5,6,7,8,9"]
        for i in numbers:
            if i not in numbers:
                return False
        return True

    def select_new_staff(self):

        id = input("Staff ID: ")
        if len(id) == 5 and id[0] == 'S' and Staff.test(self):
            if id in id_list:
                return print("The ID is taken. Please try again")
            staff_name = input("Input a name with less than 20 characters")
            while len(staff_name > 20):
                staff_name = input("Input a name with less than 20 characters")
            position = input("Input a position for the staff, Staff, Officer, or Manager")
            while position != "Staff" or position != "Officer" or position != "Manager":
                position = input("Input a position for the staff, Staff, Officer, or Manager")

            salary = input("Input a position for the staff, Staff, Officer, or Manager")
            while position == 'Staff' and int(salary) < 3500000 or int(salary) > 7000000:
                salary = input("Input a position for the staff, Staff, Officer, or Manager")

            while position == 'Officer' and int(salary) < 70000001 or int(salary) > 10000000:
                salary = input("Input a position for the staff, Staff, Officer, or Manager")

            while position == 'Manager' and int(salary) < 10000000:
                salary = input("Input a position for the staff, Staff, Officer, or Manager")


    def delete_staff(self, id):
        if id not in id_list:
            return
        del id_list[id]

    def view_summary_data(self):
        print("1. Staff:")
        print("Minimum Salary: 4500000")
        print("Minimum Salary: 5000000")
        print("Average Salary: 4750000")


        print("2. Officer:")
        print("Minimum Salary: 8500000")
        print("Minimum Salary: 8500000")
        print("Minimum Salary: 8500000")

        print("3. Manager:")
        print("Minimum Salary: 8500000")
        print("Maximum Salary: 1070000")
        print("Average Salary: 1070000")


    def save_and_exit(self):
        csv_writer = csv.writer(csv_file)
        for len(id_list):
            csv_writer.write()



with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        id_list.append(line[0])
    Staff.display_menu()
