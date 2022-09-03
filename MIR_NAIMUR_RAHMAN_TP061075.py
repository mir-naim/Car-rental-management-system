#TP061075
#MIR NAIMUR RAHMAN

import sys
from datetime import datetime
now=datetime.today().date()

#write"SUPER CAR" by using for loop
print()
print()
str1="SUPER CAR"
print_S=[[" " for i in range (5)] for j in range(7)]#row 7 and coloum 5
print_U=[[" " for i in range (5)] for j in range(7)]
print_P=[[" " for i in range (5)] for j in range(7)]
print_E=[[" " for i in range (5)] for j in range(7)]
print_R=[[" " for i in range (5)] for j in range(7)]
print_C=[[" " for i in range (5)] for j in range(7)]
print_A=[[" " for i in range (5)] for j in range(7)]

for row in range (7):
    for col in range(5):
        if ((row == 0 or  row == 3 or row == 6) and (col>0 and col<4)) or (col == 0 and (row>0 and row<3)) or (col == 4 and (row>3 and row<6)):
            print_S[row][col]="#"

for row in range(7):
    for col in range(5):
        if ((col==0 or col ==4 ) and row!=6) or (row == 6 and (col>0 and col<4)):
            print_U[row][col] = "#"

for row in range(7):
    for col in range(5):
        if col==0 or (col ==4  and (row == 1 or row ==2)) or (row==0 or row==3) and (col>0 and col<4):
            print_P[row][col] = "#"


for row in range(7):
    for col in range(5):
        if col == 0 or ((row== 0 or row== 3 or row==6) and (col>0)):
            print_E[row][col] = "#"
for row in range(7):
    for col in range(5):
        if col == 0 or (col==4 and (row!=0 and row!=3)) or ((row == 0 or row ==3) and (col>0 and col<4)):
            print_R[row][col] = "#"
for row in range(7):
    for col in range(5):
        if (col == 0 and (row!=0 and row!=6)) or ((row == 0 or row==6) and (col>0)):
            print_C[row][col] = "#"

for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row ==0 or row==3) and (col>0 and col<4)):
            print_A[row][col] = "#"

for row in range(7):
    for col in range(5):
        if col == 0 or (col==4 and (row!=0 and row!=3)) or ((row == 0 or row ==3) and (col>0 and col<4)):
            print_R[row][col] = "#"


for i in range (7):
    for j in range(5):
        print(print_S[i][j],end=" ")
    print(end="   ")
    for j in range(5):
        print(print_U[i][j], end=" ")
    print(end="   ")
    for j in range(5):
        print(print_P[i][j], end=" ")
    print(end="   ")
    for j in range(5):
        print(print_E[i][j], end=" ")
    print(end="   ")
    for j in range(5):
        print(print_R[i][j], end=" ")
    print(end="         ")
    for j in range(5):
        print(print_C[i][j], end=" ")
    print(end="   ")
    for j in range(5):
        print(print_A[i][j], end=" ")
    print(end="   ")
    for j in range(5):
        print(print_R[i][j], end=" ")
    print()


#Start system from here
def main_menu():
    print()
    print("                           WELCOME TO SUPER CAR RENTAL SYSTEM !!")
    print()
    print("                            ------------MAIN MENU-------------")
    print("                            ----------------------------------")
    print("                            ---       1- Register          ---")
    print("                            ---       2- Admin login       ---")
    print("                            ---       3- user login        ---")
    print("                            ---       4- visitor           ---")
    print("                            ---       5- Exit              ---")
    print()

    while True:
        userChoice = input("                                  Choose an option:")#choose [1,2,3,4,5].otherwise it will ask again.
        if userChoice in ['1', '2', '3', '4', '5']:
            break
    if userChoice == '1':
        Register()
    elif userChoice == '2':
        admin_login()
    elif userChoice == '3':
        login()
    elif userChoice == '4':
        visitor()
    else:
        exit()


# Register form for the users.Users need to enter name ,password and mobile number
def Register():

    print("Registration form ")
    print("------------------")
    print("------------------")
    print()
    while(True):
        username = input("Enter your Name: ")#username must be aphabetic order and cannot be empty
        if ((username >= 'a' and username <= 'z') or (username >= 'A' and username <= 'Z')) and username != '' :
            break
    while(True):
        userpassword = input("Enter your password: ")
        if userpassword != '':
            break
    while(True):
        confirmpassword= input("Confirm your password: ")#password cannot be empty
        if confirmpassword == userpassword:
            break
        else:
            print("Password don`t match")
            print()
    while True:
        mobile_number=input("Enter your valid phone number:")#Phone number should be 14 digits
        if mobile_number.isnumeric() and len(mobile_number)<14:
            break
        else:
            print("Your mobile number is not valid")

    if userAlreadyExist(username,userpassword):
        while True:
            print()
            error = input("You are already registered.\n\npress (T) to try again:\n press(L) to Login:").lower()#check username and password whether exist or not
            if error == 't':
                Register()
                break
            elif error == 'l':
                login()
                break
    new_memno ="mem"+str(len(open("userinfo.txt","r").readlines())+1)
    open("userInfo.txt","a").write(new_memno+";"+username+";"+userpassword+";"+mobile_number+"\n")#write username,password and phone number and save it to text file
    print("Successfully Registered !")
    print()
    print("press [1] - to login")
    print("press [2]- to Exit")
    print()
    while True:
        usertype = input("Enter your choice:")
        if usertype=="1":
            login()
        else:
            main_menu()

#Admin login panel.After entering valid username and password admin can enter the admin panel.

def admin_login():
    print("welcome to Admin Login page !")
    print("-----------------------------")
    print("-----------------------------")
    with open('admin_user_info.txt', 'r') as file:
        lines = file.readlines()
        while True:
            username = input("Enter your username:")#check username to the text file
            for line in lines:
                line = line[:-1]
                object = line.split(";")
                if username == object[1]:
                    userpassword = input("Enter your password:")#check username and password match or not
                    if userpassword == object[2]:
                        print()
                        print("Successfully login" + " " + username)
                        admin_login_options()
                    else:
                        print("---Incorrect password---")
                        main_menu()

# After entering admin panel admin can access all others options
def admin_login_options():
    print("Welcome to admin panel !")
    print()
    print("----Admin menu-----")
    print("------------------")
    print("1- Add rent car details")
    print("2- Modify car details")
    print("3- Display available cars for rent")
    print("4- customer payment for specific time")
    print("5- Specific car booking record")
    print("6- Add Return cars")
    print("7- Add new admin user")
    print("8- Specific customer payment details")
    print("9- Log out !")
    print()

    while True:
        userChoice = input("Choose an option: ")
        if userChoice in ['1', '2', '3', '4', '5', '6', '7','8','9']:#Take input from [1-9]
            break
    if userChoice == '1':
        add_cars()
    elif userChoice == '2':
        modify_cars()
    elif userChoice == '3':
        available_rent()
    elif userChoice == '4':
        customer_payment()
    elif userChoice == '5':
        search_record()
    elif userChoice == '6':
        return_cars()
    elif userChoice == '7':
        admin_user()
    elif userChoice == '8':
        specific_payment()
    elif userChoice =='9':
        main_menu()


#Admin Can add cars after selecting add car details.
 #Malaysian Car Number should be AX1234 or AXX1234.Car number should be 6 digit or 7 digit .
    #First number refer to State of Malaysia

def add_cars():
    print("Welcome to Add cars page !")
    print("--------------------------")
    print("--------------------------")
    while (True):
        while True:
            plate_number = input("Enter the car plate number:").upper()
            if  len(plate_number)==6 or len(plate_number)==7:
                break
            print("Invalid Input")
            admin_login_options()
        new_plate = plate_number.upper()
        if len(new_plate) == 6 :
            if new_plate[0] in ["E" , "I" , "L" , "O" , "Q" , "S" , "X" , "Y" , "Z"]:
                print("Invalid car Area Number")
            elif new_plate[1] in ["I" , "O" , "S" , "Z"]:
                print("Car number cannot be I O Z")
            elif new_plate[2:6].isnumeric()==False:
                print("Invalid car Number !")
            else:
                break

        elif len(new_plate) == 7 :
            if new_plate[0] in ["E" , "I" , "L" , "O" , "Q" , "S" , "X" , "Y" , "Z"]:
                print("Invalid car Area Number")
            elif new_plate[1] in ["I" , "O" , "S" , "Z"]:
                print("Car number cannot be I O Z")
            elif new_plate[2] in ["I" , "O" , "S" , "Z"]:
                print("Car number cannot be I O Z")
            elif new_plate[3:7].isnumeric() == False:
                print("Invalid car Number !")
            else:
                break

    while (True):
        car_name = input("Enter your car name: ").title()
        if car_name != '':
            break
    while (True):
        car_colour = input("Enter your car colour: ").title()
        if car_colour != '':
            break
    while (True):
        car_seats = input("Enter your car seats: ")
        if car_seats != '':
            break
    while (True):
        try:
            car_price = int(input("Enter your car rent price per day (RM): "))#car price cannot be string.
            if car_price != '':
                break
        except:
            print("Enter the valid number")

    while(True):
        car_owner = input("Enter the car owner name: ").title()
        if car_owner != '':
            break

    carno="car"+str(len(open("car_details.txt","r").readlines())+1)#write car details to the car-details text file.[car] is unique id
    open("car_details.txt","a").write(carno+";"+plate_number+";"+car_name+";"+car_colour+";"+car_seats+";"+str(car_price)+";"+car_owner+";Available\n")
    print()

    print("Successfully added the car details")
    print()

    #Go back to admin menu
    print("Press[1] - Go to Admin menu")
    print("press[2] - Exit")
    while True:
        usertype=input("Choose as an option:")
        print()
        if usertype == "1":
            admin_login_options()
        else:
            main_menu()


#After taking input about the car details ,it will save a text file named car_details.txt.
#Modify car details with car number
def modify_cars():
    mylist = []
    car_id = input("Enter the car ID number to modify the record :")
    fh=open("car_details.txt", "r").readlines()#show the text file
    for record in fh:
        reclist = record.rstrip().split(";")
        if car_id == reclist[0]:
            print("1. Car name is  : ", reclist[2])
            print("2. Car Colour is: ", reclist[3])
            print("3. car seats : ", reclist[4])
            print("4. Car price per day is: ", reclist[5])
            print("5. Car owner name is: ", reclist[6])



            try:
                getind = int(input("Enter the Field no. to modify :"))#input should be integer

                reclist[getind + 1] = input("\n\nEnter the new value :").title()
                print("--Successfully modified--")
            except:
                print("Invalid Input")

        mylist.append(reclist)


    with open("car_details.txt", "w") as fh:
        for rec in mylist:
            recstr = ";".join(rec)
            fh.write(recstr + "\n")
    admin_login_options()




#Read car details from text file car_details.txt
def available_rent():
    print("Car Number  Car Name    Colour      Seats       Price       Owner       Price per Day")
    print("--------------------------------------------------------------------------------------")
    cars=open("car_details.txt","r").readlines()        #cars=list
    for car in cars:
        car=car[:-1]
        items=car.split(";")             #item=list
        for item in items:
            print(item.ljust(12),end="")#ljust use for  give space from left sid
        print("")
    print()
    print("Press[1] - Go to Admin menu")
    print("press[2] - Log out !")
    while True:
        usertype = input("Choose as an option:")
        print()
        if usertype == "1":
            admin_login()
        else:
            main_menu()


def customer_payment():
    while True:
        start_date = input("Enter the start date(DD.MM.YYYY): ")
        try:
            date1 = datetime.strptime(start_date, "%d.%m.%Y")#string convert into datetime
            break
        except:
            print("Invalid date format")
    while True:
        end_date = input("Enter the end date:(DD.MM.YYYY): ")
        try:
            date2 = datetime.strptime(end_date, "%d.%m.%Y")
            break
        except:
            print("Invalid date format")

    if date1 > date2:
        print("Error:")#start date cannot be bigger than end date
    elif date1 < date2:
        print("DATE IS VALID")
        # PRINT LINES BETWEEN THEESE TWO DATES

    print("Payment Number  Booking Date    Member Number   User Name       Book Number      Total Days      Total Cost  ")
    print("----------------------------------------------------------------------------------------------------------")
    cars = open("payment_details.txt", "r").readlines()  # cars=list
    for car in cars:
        car = car[:-1]
        items = car.split(";")  # item=list
        l_date = datetime.strptime(items[1], "%Y-%m-%d")#match with the date and show result
        if date1<=l_date<=date2:
            for item in items:
                print(item.ljust(16), end="")
            print("")
    print()
    print("Press[1] - Go to Admin menu")
    print("press[2] - Log out !")
    while True:
        usertype = input("Choose as an option:")
        print()
        if usertype == "1":
            admin_login_options()
        else:
            main_menu()


#Search each car details by putting car plate number only
#one car details at a time
def search_record():
    mylist = []
    with open("booking_car.txt", "r") as fh:
        car_id = input("Enter the Car ID to search the specific car booking record :").lower()#Enter car number to see details
        for record in fh:
            reclist = record.rstrip().split(";")
            if car_id in reclist[4]:
                print("1. Car Booking Number is : ", reclist[0])
                print("2. Car  Booking Date is  : ", reclist[1])
                print("3. Car Owner name is : ", reclist[3])
                print("4. car Booking for  : ", reclist[5])
                print("5. Car rent total price is: ", reclist[6])
                break

        ans = input("7. Back to Admin menu:")
        if ans == "7":
            admin_login_options()
        else:
            main_menu()


#For return back ,admin has to write Available.Then it will able to book for the users
def return_cars():
    mylist = []
    with open("car_details.txt") as fh:
        car_id=input("Enter the car ID number:").lower()
        for record in fh:
            reclist=record.rstrip("\n").split(";")
            if car_id in reclist[0]:
                print("Car Id      Car Number  Car Name    Car Color   Car seat     Car Price   Car owner   car status  ")
                print("----------------------------------------------------------------------------------")
                cars = open("car_details.txt", "r").readlines()  # cars=list
                for car in cars:
                    car = car[:-1]
                    items = car.split(";")  # item=list
                    for item in items:
                        print(item.ljust(12), end="")
                    print("")
                reclist[7]=input("Write [Available] for showing back to rent:").title()
                print("Successfully added for rent")
            mylist.append(reclist)#Append Available on the rent car list

    with open("car_details.txt", "w") as fh:
        for ind in range(len(mylist)):
            recstr = ";".join(mylist[ind])
            fh.write(recstr + "\n")

    admin_login_options()




#Only from admin panel ,admin can register for new admin users.
def admin_user():
    print("Admin user registration form ")
    print("-----------------------------")
    print()
    while (True):
        userName = input("Enter your Name:")
        if userName != '':
            break
    while (True):
        userPassword = input("Enter your password:")
        if userPassword != '':
            break
    while (True):
        confirmpassword = input("Confirm your password:")
        if confirmpassword == userPassword:
            break
        else:
            print("Password don`t match")
            print()
    while True:
        mobile_number = input("Enter your valid phone number:")
        if mobile_number.isnumeric() and len(mobile_number) < 14:
            break
        else:
            print("Your mobile number is not valid")

    if admin_user_exist(userName,userPassword):
        while True:
            print()
            error = input("You are already registered.\n\nPress (1) to Admin Login :\n Press(2) to Exit:").lower()
            if error == '1':
                admin_login()
                break
            else:
                exit()

    New_num = "Admin" + str(len(open("admin_user_info.txt", "r").readlines()) + 1)#admin has unique id
    open("admin_user_info.txt", "a").write(New_num + ";" + userName + ";" + userPassword + ";" + mobile_number + "\n")
    print("Successfully Registered !")
    print()
    print("press[1]- to Admin login")
    print("press[2]- to Log out")
    print()

    while True:
        usertype = input("Enter your choice:")
        if usertype == "1":
            admin_login()
        else:
            main_menu()

#Admin can see spesific customer payment by enter booking id
def specific_payment():
    while True:
        start_date = input("Enter the start date(DD.MM.YYYY): ")
        try:
            date1 = datetime.strptime(start_date, "%d.%m.%Y")
            break
        except:
            print("Invalid date format")
    while True:
        end_date = input("Enter the end date:(DD.MM.YYYY): ")#Date should be correct order.Otherwise it will go to except section.
        try:
            date2 = datetime.strptime(end_date, "%d.%m.%Y")
            break
        except:
            print("Invalid date format")
    while True:
        user_id_no=input("Enter your member ID Number:")
        if user_id_no != "":
            break


    if date1 > date2:
        print("Error:")
    elif date1 < date2:
        print("DATE IS VALID")
        # PRINT DATA BETWEEN THEESE TWO DATES

    print(
        "Payment Number  Booking Date    Member Number   User Name       Booking Num     Total Days      Total Cost  ")
    print("----------------------------------------------------------------------------------------------------------")
    cars = open("payment_details.txt", "r").readlines()  # cars=list
    for car in cars:
        car = car[:-1]
        items = car.split(";")  # item=list
        l_date = datetime.strptime(items[1], "%Y-%m-%d")
        if date1 <= l_date <= date2 and user_id_no ==items[3]:
            for item in items:
                print(item.ljust(16), end="")
            print("")

    print()
    print("Press[1] - Go to Admin menu")
    print("press[2] - Log out !")
    while True:
        usertype = input("Choose as an option:")
        print()
        if usertype == "1":
            admin_login_options()
        else:
            main_menu()



#Login panel for users.Users need to enter name and password mendatory.
def login():
    print("welcome to User Login Page!")
    print("---------------------------")
    print("---------------------------")
    with open('userInfo.txt', 'r') as file:
        lines = file.readlines()
        while True:
            username = input("Enter your username:")
            for line in lines:
                line = line[:-1]
                object = line.split(";")
                if username == object[1]:
                    userpassword=input("Enter your password:")
                    if userpassword==object[2]:
                        print()
                        print("Successfully login " + username)
                        login_options(object[0],object[1])
                    else:
                        print("---Incorrect password---")
                        main_menu()
            main_menu()

#User login options for avoiding login username and password again and again
def login_options(member,name):
    while True:
        print()
        print( "Welcome to user login panel !")
        print("------------------------------")
        print("1- view all cars available for rent")
        print("2- Personal Rental History")
        print("3- View details of rental car")
        print("4- Select and book car on specific time")
        print("5- payment for booking")
        print("6- Log out !")
        print()
        while True:
            userChoice = input("Choose an option: ")
            if userChoice in ['1', '2', '3', '4', '5', '6']:
                break
            else:
                print("Please Try again")
        if userChoice == '1':
            print("Car Number  Car Name    Colour      Seats       Price       Owner       Price per Day    Car Status   ")
            print("----------------------------------------------------------------------------------------------------")
            cars = open("car_details.txt", "r").readlines()  # cars=list
            for car in cars:
                car = car[:-1]
                items = car.split(";")  # item=list
                for item in items:
                    print(item.ljust(12), end="")
                print("")
            print()
            print("Press[1] - Booking a car")
            print("Press[2] - Go to login  menu")
            print("press[3] - Log Out !")
            while True:
                usertype = input("Choose as an option:")
                print()
                if usertype == "1":
                    book_car(member,name)
                elif usertype=="2":
                    login_options(member, name)
                else:
                    main_menu()
                break


        elif userChoice == '2':
            personal_rent(member,name,member)
        elif userChoice == '3':
            details_of_rent_car(name,member)
        elif userChoice == '4':
            book_car(member,name)
        elif userChoice == '5':
            payment_car(name,member)
        else:
            main_menu()
        break

#user can see only their booking cars
def personal_rent(rent,name,member):
    print("Booking No     Booking Date   Member Num      Booker Name       Car ID          Duration       Price        ")
    print("------------------------------------------------------------------------------------------------")
    bookingcar = open("booking_car.txt", "r").readlines()  # cars=list
    for car in bookingcar:
        car = car[:-1]
        items = car.split(";")  # item=list
        if items[2]==rent:#match with user information
            for item in items:
                print(item.ljust(15), end="")
            print("")
    print()
    print("1- payment of booking car")
    print("2- Login out !")
    while True:
        choice = input("Choose an option:")
        if choice=="1":
            payment_car(name, member)
        elif choice=="2":
            main_menu()
        else:
            print("Invalid Input")
        break




#Details of car by enter car plate number
def details_of_rent_car(name,member):
    mylist = []
    with open("car_details.txt", "r") as fh:
        car_id = input("Enter the Car ID to see the specific car details :").lower()
        for record in fh:
            reclist = record.rstrip().split(";")
            if car_id in reclist[0]:
                print("1. Car Plate Number is : ", reclist[1])
                print("2. Car name is  : ", reclist[2])
                print("3. Car Colour is: ", reclist[3])
                print("4. car seats : ", reclist[4])
                print("5. Car price per day is: ", reclist[5])
                print("6. Car owner name is: ", reclist[6])
                break

        ans = input("7. Back to Login menu:")
        if ans == "7":
            login_options(member,name)
        else:
            main_menu()



#Car booking function
def book_car(member,name): #member,name -parameter
    print()
    cars = open("car_details.txt", "r").readlines()
    car_list = []
    while True:
        car_number = input("Enter the Car ID that you want to book:").lower()#car ID number example car1
        if car_number.isalnum()== True:
            break
        else:
            print("Invalid Number")
    for car in cars:
        car=car[:-1]
        details = car.split(";")
        if car_number == details[0]:#check with car ID number
            if details[7] == "Available":
                print(details[0],"Details of"":")
                print()
                print("1. Car Plate Number is : " +details[1])
                print("2. Car name is  : " +details[2])
                print("3. Car Colour is: " +details[3])
                print("4. car seats : " +details[4])
                print("5. Car price per day is: " +details[5])
                print("6. Car owner name is: " +details[6])
                print("-----------------------------------")
                print("------------------------------------")
                print("Do you want to book this car ?")
                print("press")
                print("[Y]-Yes; if you want to book")
                print("[N]-No; if you want to cancel")

                while True:
                    choice=input("Enter your choice:").lower()
                    if choice =="y" or choice=="n":
                        break
                    print("Invalid input")
                if choice=="y":
                    while True:
                        time_duration=input("Enter the time duration (Days) you want to rent:")
                        if time_duration.isnumeric()== True:
                            break
                        print("Enter number only !")
                    time_duration=int(time_duration)
                    price=int(details[5])
                    total = time_duration * price
                    print()
                    print("The total payment is:",time_duration,"Days * RM",price," =  RM",total)
                    print("Press [Y] to confirm booking")
                    print("press[N] to cancel booking")
                    while True:
                        choice1 =input("Enter the choice(Y/N):").lower()
                        if choice1=="y" or "n":
                            break
                    if choice1 =="y":
                        details[7]="Booking by" + member
                        record_number=len(open("booking_car.txt","r").readlines()) +1
                        booknum="Book" + str(record_number)
                        days=str(time_duration) + "Days"
                        RM= "RM" + str(total)
                        open("booking_car.txt","a").write(booknum+";"+str(now)+";"+member+";"+name+";"+details[0]+";"+days+";"+RM+"\n")
                        open("booking_car.txt","a").close()#Append in booking_car.txt
                        print("")
                        print("--Booking Successful--")
                    elif choice1=="n":
                        print("Booking cancel")
                        return
                elif choice == "n":
                    print("Booking cancel")
                    return
        car_list.append(details)
    with open("car_details.txt","w") as wr:
        for add in car_list:
            added=";".join(add)
            added=added+"\n"
            wr.write(added)
        wr.close()


#After payment payment id will generate
#payment car function
def payment_car(member,name):#parameter member,name
    print()
    payment = open("booking_car.txt", "r").readlines()
    pay_list = []
    while True:
        book_id = input("Enter the booking number to  make payment:").title()#Booking Id Example -Book1
        if book_id.isalnum() == True:
            break
        else:
            print("Invalid Number")
    for pay in payment:
        pay = pay[:-1]
        payment_details = pay.split(";")
        if book_id == payment_details[0]:
            rent_money=input("Enter your total money:")
            if payment_details[6][2:] == rent_money:#payment_details=list
                print( "Details of:"+payment_details[0])
                print()
                print("1. Car book date : " + payment_details[1])
                print("2. user member name  : " + payment_details[2])
                print("4. car unique number : " + payment_details[4])
                print("5. Car rented  day : " + payment_details[5])
                print("6. Car rented total price : " + payment_details[6])
                print("-----------------------------------")
                print("------------------------------------")
                record_number = "pay"+str(len(open("payment_details.txt", "r").readlines()) + 1)
                open("payment_details.txt", "a").write(record_number + ";" + str(now) + ";" +member+ ";" +name+ ";" + payment_details[0] + ";" + payment_details[5] + ";" + payment_details[6] + "Paid" "\n")
                open("payment_details.txt", "a").close()
                print("")
                print("--Paid Successful--")

        pay_list.append(payment_details)


#visitors can see view all cars ,and register as a user
#Visitors panel for the users.users can also register from here
def visitor():
    print("Hello Stranger ! welcome to super car system")
    print("-----------------------------------------------")

    while (True):
        print("press:")
        print("[1]-to view cars available for rent")
        print("[2]-to register as a new member")
        print("[3]-to go back Main Menu")
        usertype = input("please enter your choice:")
        if (usertype == "1" or usertype == "2" or usertype == "3"):
            break
        print("Invalid input ! Try Again")
    if (usertype == "1"):
        print("Car ID       Car Number   Car Name   colour    seats     Price day     Owner       car status    ")
        print("----------------------------------------------------------------------------------------------")
        cars = open("car_details.txt", "r").readlines()  # cars=list
        for car in cars:
            car = car[:-1]
            items = car.split(";")  # item=list
            for item in items:
                print(item.ljust(12), end="")
            print("")
        print()
        print("Press[1] - Go to main menu")
        print("press[2] - Exit !")
        while True:
            usertype = input("Choose as an option:")
            print()
            if usertype == "1":
                main_menu()
            else:
                exit()

        while True:
            usertype=input("Choose an option:")
            print()
            if(usertype == "1"):
                main_menu()
            else:
                exit()

    elif(usertype == "2"):
        Register()
    elif(usertype == "3"):
        main_menu()
    else:
        exit()



#If users detaails have already exit .Then show it you have been already exit
def userAlreadyExist(username ,userpassword):
    userpassword =(userpassword)
    usersInfo = {}
    with open('userInfo.txt','r') as file :#check username and password with text file ,already exist or not.
        for line in file :                 #If exist ,it will show already registerd
            line =line.split(";")
            if line[1]== username and line[2] == userpassword:
                usersInfo.update({line[1]:line[2]})
    if usersInfo == {}:
        return False
    return usersInfo[username]== userpassword


#Admin user login information exit or not
def admin_user_exist(userName ,userPassword):
    userPassword =(userPassword)
    usersInfo = {}
    with open('admin_user_info.txt','r') as file :#check with text file username and password already exist or not
        for line in file :
            line =line.split(";")
            if line[1]== userName and line[2] == userPassword:
                usersInfo.update({line[1]:line[2]})
    if usersInfo == {}:
        return False
    return usersInfo[userName]== userPassword


main_menu()


