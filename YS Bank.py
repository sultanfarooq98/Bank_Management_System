import csv

with open("bank_data.csv", "w", newline="") as write_f:
    header = ['Name', 'Password', 'Phone', "CNIC", "Balance"]
    write = csv.DictWriter(write_f, fieldnames=header, delimiter=",")
    write.writeheader()
import getpass

print("Welcome To YS Bank")
print()


def new_account():
    while True:
        name = input("Enter Name: ")
        if name == "" or name == " ":
            print("Invalid Input, Try Again.")
        else:
            break

    while True:
        password = getpass.getpass("Enter Password : ")
        if len(password) < 5:
            print("Password lenght should be atleast 5 characters.")
            continue
        for i in password:
            if i == " ":
                print("Please don't enter any spaces in your password.")
                break
            continue
        else:
            break

    while True:
        Phone = input("Enter your Phone No. : ")
        if (len(Phone) != 11):
            print("Lenght must be 11")
        else:
            break

    while True:
        while True:
            cnic_1 = input("Input the frist \"5\" digits of CNIC: ")
            if len(cnic_1) != 5:
                print("The lenght must be 5.")
                continue
            else:
                break

        while True:
            cnic_2 = input("Input the middle digits of the CNIC: ")
            if len(cnic_2) != 7:
                print("The middle numbers lenght must be 7.")
                continue
            else:
                break

        while True:
            cnic_3 = input("Input the last digit of the CNIC: ")
            if len(cnic_3) != 1:
                print("The lenght must be 1.")
                continue
            else:
                break

        cnic = cnic_1 + "-" + cnic_2 + "-" + cnic_3
        break

    while True:
        balance = int(input("How much Money you want to save : "))
        if balance < 1000:
            print("Dear Sir you must submit atleast 1000 Rs.")
        else:
            break

    with open("bank_data.csv", "a", newline="") as append_file:
        header = ['Name', 'Password', 'Phone', "CNIC", "Balance"]
        write = csv.DictWriter(append_file, fieldnames=header, delimiter=",")
        write.writerow({"Name": name, "Password": password, "Phone": Phone, "CNIC": cnic, "Balance": balance})
        print("Congratulations, Your account has been successfully created.")


def authentication():
    condition = False
    name = input("Enter name: ")
    password = getpass.getpass("Enter password: ")

    with open("bank_data.csv", "r") as read_f:
        csv_reader = csv.DictReader(read_f, delimiter=",")
        for line in csv_reader:
            if line["Name"] == name and line["Password"] == password:
                print("Authentication successful!")
                condition = True
                break
        else:
            print("Authentication failed!")
            condition = False
    return name, password, condition


def Working():
    while True:
        choice = input("Log In(L/l) or Create new account(N/n): ")
        if choice == "l" or choice == "L":
            name, password, condition = authentication()
            if condition == True:
                break
            else:
                continue
        elif choice == "n" or choice == "N":
            new_account()
            continue
        else:
            print("Wrong Entry.")

    while True:
        option = input("A) Deposit \nB) Withdraw \nC) Check Balance \nD) Quit \nSelect Option: ")
        if option == 'A' or option == 'a':
            while True:
                deposit = int(input("Amount to deposit is: "))
                if deposit > 0:
                    break
                else:
                    print("Wrong Input")

            with open("bank_data.csv", "r", newline="") as read_f:
                read = csv.DictReader(read_f, delimiter=",")
                bank_data = list(read)
            with open("bank_data.csv", "w", newline="") as write_f:
                head = ["Name", "Password", "Phone", "CNIC", "Balance"]
                write = csv.DictWriter(write_f, fieldnames=head, delimiter=",")
                write.writeheader()
                for line in bank_data:
                    if line["Name"] == name and line["Password"] == password:
                        new_balance = str(int(line["Balance"]) + deposit)
                        write.writerow({"Name": line["Name"], "Password": line["Password"], "Phone": line["Phone"],
                                        "CNIC": line["CNIC"], "Balance": new_balance})
                        print(
                        "The amount has been sussesfuly deposited into your account your new balance is: ", new_balance)
                    else:
                        write.writerow({"Name": line["Name"], "Password": line["Password"], "Phone": line["Phone"],
                                        "CNIC": line["CNIC"], "Balance": line["Balance"]})

        elif option == 'B' or option == 'b':
            while True:
                withdraw = int(input("The money you want to withdraw: "))
                if withdraw > 0:
                    with open("bank_data.csv", "r") as read_f:
                        read = csv.DictReader(read_f, delimiter=",")
                        for line in read:
                            if line["Name"] == name and line["Password"] == password:
                                if withdraw > int(line["Balance"]):
                                    print(
                                        "Dear Sir, your current balance is \"{}\" so you cannot withdraw \"{}\" amount.".format(
                                            line["Balance"], withdraw))
                                    break
                                continue
                        else:
                            break
                else:
                    print("Wrong Input.")

            with open("bank_data.csv", "r", newline="") as read_f:
                read = csv.DictReader(read_f, delimiter=",")
                read_list = list(read)
            with open("bank_data.csv", "w", newline="") as write_f:
                head = ["Name", "Password", "Phone", "CNIC", "Balance"]
                write = csv.DictWriter(write_f, fieldnames=head, delimiter=",")
                write.writeheader()
                for line in read_list:
                    if line["Name"] == name and line["Password"] == password:
                        new_amount = str(int(line["Balance"]) - withdraw)
                        write.writerow({"Name": line["Name"], "Password": line["Password"], "Phone": line["Phone"],
                                        "CNIC": line["CNIC"], "Balance": new_amount})
                        print(
                        "The amount has been sussesfuly withdrawn from your account your new balance is: ", new_amount)
                    else:
                        write.writerow({"Name": line["Name"], "Password": line["Password"], "Phone": line["Phone"],
                                        "CNIC": line["CNIC"], "Balance": line["Balance"]})

        elif option == "C" or option == "c":
            with open("bank_data.csv", "r") as read_f:
                read = csv.DictReader(read_f, delimiter=",")
                for line in read:
                    if line["Name"] == name and line["Password"] == password:
                        print("Dear Sir, \n")
                        print("Name: ", line["Name"])
                        print("Balance: ", line["Balance"])
                        break

        elif option == "D" or option == "d":
            break


Working()