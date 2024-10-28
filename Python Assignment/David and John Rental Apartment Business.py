#YAU KAI JOON #TP64474
#LIM YEE ERN #TP065084

def Main_menu():
    while True:
        print(
            "========================================================================================================================================================================================================================================================================================\n"
            "========================================================================================================================================================================================================================================================================================\n"
            "\t                                                              * WELCOME TO DAVID & JOHN RENTAL APARTMENT BUSINESS *         \n"
            "========================================================================================================================================================================================================================================================================================\n"
            "========================================================================================================================================================================================================================================================================================\n")


        print("PLEASE SELECT ONE OF THE NUMBER BELOW TO GET MORE INFORMATION")
        option = int(input("\n1. LOGIN & REGISTRATION."
                        "\t\t2. PAYMENT."
                        "\n\nPLEASE SELECT A NUMBER TO PROCEED:"))
        break

    if option == 1:
        LoginAndRegistrationForm()
    elif option == 2:
        PaymentForm()

#LOGIN & REGISTRATION (FIST OPTION UNDER Main_menu)

def LoginAndRegistrationForm():
    rec = []
    with open("File.txt", "r") as fh:
        for lines in fh:
            list=lines.split(",")
            rec.append(list)
    while True:
        print("\n----------------------------------------------------------------\n"
              "\t                 LOGIN & REGISTRATION MENU                                 \n"
              "----------------------------------------------------------------    \n")
        print("SELECT A NUMBER IN LOGIN & REGISTRATION MENU:")
        option = int(input("\n1. LOGIN."
                            "\t\t2. REGISTER."
                            "\n\nPLEASE SELECT A NUMBER TO PROCEED:"))

        if option == 1:
            Login(rec)

        elif option == 2:
            data=Register()
            rec.append(data)
            return Login(rec)
        else:
            print("PLEASE SELECT A NUMBER TO PROCEED:")

def Register():
    print("\n----------------------------------------------------------------\n"
          "\t                PLEASE REGISTER AN ACCOUNT                 \n"
          "----------------------------------------------------------------\n")
    temp=1
    while temp==1:
        username = input("PLEASE ENTER A NEW USERNAME:")
        if len(username) < 2:
            print("Your Username Is Too Short!")
            temp=1
        elif len(username) > 13:
            print("Your Username Is Too Long!")
            temp=1
        else:
            temp=0
            temp1=1
            while temp1 == 1:
                password = input("CREATE A NEW PASSWORD:")
                symbol = ['!','@', '#', '$', '%', '^', '&', '*']
                if len(password) < 5:
                    print("Your Password Is Too Short!")
                    temp1=1
                elif len(password) > 10:
                    print("Please Shorten Your Password, It's Too Long!")
                    temp1=1
                elif not any(char.isdigit()for char in password):
                    print("Your Password Should Contain At Least One Numeral!")
                    temp1=1
                elif not any(char.isupper()for char in password):
                    print("Your Password Should Contain At Least One Capital Letter!")
                    temp1=1
                elif not any(char.islower()for char in password):
                    print("Your Password Should Contain At Least One Lower Letter!")
                    temp1=1
                elif not any(char in symbol for char in password):
                    print("Your Password Should Have At Least One Symbol!")
                    temp1=1
                else:
                    temp1=0
                    temp2=1
                    while temp2==1:
                        password1 = input("PLEASE RE-CONFIRM YOUR PASSWORD:")
                        if password1 == password:
                            print("\nWELCOME, " + username + ". YOU HAVE SUCCESSFULLY REGISTERED AN ACCOUNT!\n")
                            print("Your Username is " + username,"|","Your Password is " + password)
                            temp2=0
                        elif password1 != password:
                            print("Kindly Please Try Again... Your Password Is Not Match!")
                            temp2=1
    with open("File.txt", "a") as file:
        user = []
        user.append(username)
        user.append(password)
        file.write(",".join(user) + "\n")
        return user

def Login(rec):
    print("\n----------------------------------------------------------------\n"
          "\t                  PLEASE LOG IN TO YOUR ACCOUNT                 \n"
          "----------------------------------------------------------------\n")
    user = len(rec)
    while True:
        Username = input("ENTER YOUR USERNAME:")
        for i in range(user):
            if Username in rec[i][0]:
                Password = input("ENTER YOUR PASSWORD:")
                if (Password in rec[i][1]):
                    print("\nLOGIN SUCCESS")
                    print("\nHI IT'S GOOD TO SEE YOU AGAIN,", Username)
                    option = int(input("\n1. GUEST VIEW."
                                       "\t\t2. MODIFY."
                                       "\t\t3. EXIT TO MAIN MENU."
                                       "\n\nPLEASE SELECT A NUMBER TO PROCEED:"))
                    if option == 1:
                        Guest()
                    elif option == 2:
                        Modify()
                    elif option == 3:
                        return Main_menu()
                else:
                    print("Invalid Password!")

def Guest():
    print("\n----------------------------------------------------------------\n"
        "\t                       GUEST MENU                                 \n"
        "----------------------------------------------------------------    \n")
    print("SELECT A NUMBER IN GUEST VIEW:")

    option = ()
    while True:
        option = int(input("\n1. DISPLAY TENANT DETAILS."
                            "\t2. DISPLAY APARTMENT DETAILS."
                            "\t3. DISPLAY PAST TENANT DETAILS.\n\n"
                            "PLEASE SELECT A NUMBER TO PROCEED:"))
        break

    if option == 1:
       Tenant()
    elif option == 2:
        Apartment()
    elif option == 3:
        PastTenant()
    else:
        print("PLEASE SELECT A NUMBER TO PROCEED")

def Tenant():
    print("\n----------------------------------------------------------------\n"
          "\t                  DISPLAY TENANT DETAILS                        \n"
          "----------------------------------------------------------------  ")

    file="Tenant.txt"
    f=open(file,'r+')
    text=f.read()
    print(text)
    f.close()

    option = ()
    while True:
        option = int(input("\n1. EXIT TO MAIN MENU."
                           "\t\t2. EXIT TO GUEST MENU."
                           "\t\tPLEASE SELECT A NUMBER TO PROCEED:"))
        break

    if option == 1:
        return Main_menu()
    elif option == 2:
        return Guest()

def Apartment():
    print("\n----------------------------------------------------------------\n"
          "\t                  DISPLAY APARTMENT DETAILS                     \n"
          "----------------------------------------------------------------  ")

    file="Apartment.txt"
    f=open(file,'r+')
    text=f.read()
    print(text)
    f.close()

    option = ()
    while True:
        option = int(input("\n1. EXIT TO MAIN MENU."
                           "\t\t2. EXIT TO GUEST MENU."
                           "\t\tPLEASE SELECT A NUMBER TO PROCEED:"))
        break

    if option == 1:
        return Main_menu()
    elif option == 2:
        return Guest()

def PastTenant():
    print("\n----------------------------------------------------------------\n"
          "\t                  DISPLAY PAST TENANT DETAILS                   \n"
          "----------------------------------------------------------------  ")

    file="Past Tenant.txt"
    f=open(file,'r+')
    text=f.read()
    print(text)
    f.close()

    option = ()
    while True:
        option = int(input("\n1. EXIT TO MAIN MENU."
                           "\t\t2. EXIT TO GUEST MENU."
                           "\t\tPLEASE SELECT A NUMBER TO PROCEED:"))
        break

    if option == 1:
        return Main_menu()
    elif option == 2:
        return Guest()

def Modify():
    print("\n----------------------------------------------------------------\n"
        "\t                         MODIFY MENU                                 \n"
        "----------------------------------------------------------------    \n")
    print("SELECT A NUMBER IN MODIFY:")
    option = ()
    while True:
        option = int(input("\n1. MODIFY TENANT DETAILS."
                        "\t\t2. MODIFY APARTMENT DETAILS."
                        "\t\t3. MODIFY PAST TENANT DETAILS."
                        "\n\nPLEASE SELECT A NUMBER TO PROCEED:"))
        break

    if option == 1:
        ModifyTenant()
    elif option == 2:
        ModifyApartment()
    elif option == 3:
        ModifyPastTenant()

def ModifyTenant():
    import os

    while (True):
        print("\n1) CREATE RECORD.")
        print("\n2) UPDATE RECORD.")
        print("\n3) DELETE RECORD.")
        print("\n4) FIND  SPECIAL ROOM NUMBER.")
        print("\n5) EXIT TO MAIN MENU.")
        ch = int(input("\nENTER YOUR CHOICE:"))

        if ch == 1:
            print()
            fh_w = open("Tenant.txt", "a+")
            room = input("Enter room number:")
            name = input("Enter tenant name:")
            age = input("Enter tenant age:")
            Phone_no = input("Enter tenant phone number:")
            Email = input("Enter tenant email:")
            P_O_B = input("Enter place of birth:")
            C_O_B = input("Enter city of birth:")
            Work_pos = input("Enter work position of tenant:")
            Emp = input("Enter employer of tenant:")
            fh_w.write(
                room + "|" + name + "|" + age + "|" + Phone_no + "|" + Email + "|" + P_O_B + "|" + C_O_B + "|" + Work_pos + "|" + Emp + "\n")
            fh_w.close()
            print("Tenant added!")
        if ch == 2:

            fh_r = open("Tenant.txt", "r")
            fh_w = open("temp.txt", "w")

            room = int(input("Enter room number to search:"))

            s = ' '
            while (s):
                s = fh_r.readline()
                L = s.split("|")
                if len(s) > 0:
                    if int(L[0]) == room:
                        room = input("Enter room number:")
                        name = input("Enter tenant name:")
                        age = input("Enter tenant age:")
                        Phone_no = input("Enter tenant phone number:")
                        Email = input("Enter tenant email:")
                        P_O_B = input("Enter place of birth:")
                        C_O_B = input("Enter city of birth:")
                        Work_pos = input("Enter work position of tenant:")
                        Emp = input("Enter employer of tenant:")
                        fh_w.write(
                            room + "|" + name + "|" + age + "|" + Phone_no + "|" + Email + "|" + P_O_B + "|" + C_O_B + "|" + Work_pos + "|" + Emp + "\n")
                    else:
                        fh_w.write(s)

            fh_w.close()
            fh_r.close()
            os.remove("Tenant.txt")
            os.rename("temp.txt", "Tenant.txt")

        if ch == 3:
            fh_r = open("Tenant.txt", "r")
            fh_w = open("temp.txt", "w")

            room = int(input("Enter room number to delete:"))

            s = ' '
            while (s):
                s = fh_r.readline()
                L = s.split("|")
                if len(s) > 0:
                    if int(L[0]) != room:
                        print("Delete successful!")
                        fh_w.write(s)

            fh_w.close()
            fh_r.close()
            os.remove("Tenant.txt")
            os.rename("temp.txt", "Tenant.txt")
        if ch == 4:
            fh = open("Tenant.txt", "r")
            word = input("Enter Room Number:")
            s = ""
            count = 1

            L = fh.readlines()

            for i in L:
                L2 = i.split()
                if word in L2:
                    print("Room Number", count, ":", i)

                count += 1
        if ch == 5:
            return Main_menu()

def ModifyApartment():
    import os

    while (True):
        print("\n1) CREATE RECORD.")
        print("\n2) UPDATE RECORD.")
        print("\n3) DELETE RECORD.")
        print("\n4) EXIT TO MAIN MENU.")
        ch = int(input("\nENTER YOUR CHOICE:"))

        if ch == 1:
            print()
            fh_w = open("Apartment.txt", "a+")
            room = input("Enter room number:")
            name = input("Enter tenant name:")
            date = input("Enter Date of rent:")
            Square_F = input("Enter Square footage:")
            rent = input("Enter expected rent:")
            history = input("Enter number of rent history:")
            fh_w.write(room + "|" + name + "|" + date + "|" + Square_F + "|" + rent + "|" + history + "\n")
            fh_w.close()
            print("Record added!")
        if ch == 2:

            fh_r = open("Apartment.txt", "r")
            fh_w = open("temp.txt", "w")

            room = int(input("Enter room number to search:"))

            s = ' '
            while (s):
                s = fh_r.readline()
                L = s.split("|")
                if len(s) > 0:
                    if int(L[0]) == room:
                        room = input("Enter room number:")
                        name = input("Enter tenant name:")
                        date = input("Enter Date of rent:")
                        Square_F = input("Enter Square footage:")
                        rent = input("Enter expected rent:")
                        history = input("Enter number of rent history:")
                        fh_w.write(room + "|" + name + "|" + date + "|" + Square_F + "|" + rent + "|" + history + "\n")
                    else:
                        fh_w.write(s)

            fh_w.close()
            fh_r.close()
            os.remove("Apartment.txt")
            os.rename("temp.txt", "Apartment.txt")

        if ch == 3:
            fh_r = open("Apartment.txt", "r")
            fh_w = open("temp.txt", "w")

            room = int(input("Enter room number to delete:"))

            s = ' '
            while (s):
                s = fh_r.readline()
                L = s.split("|")
                if len(s) > 0:
                    if int(L[0]) != room:
                        print("Delete successful!")
                        fh_w.write(s)

            fh_w.close()
            fh_r.close()
            os.remove("Apartment.txt")
            os.rename("temp.txt", "Apartment.txt")
        if ch == 4:
            return Main_menu()

def ModifyPastTenant():
    import os

    while (True):
        print("\n1) CREATE RECORD.")
        print("\n2) UPDATE RECORD.")
        print("\n3) DELETE RECORD.")
        print("\n4) EXIT TO MAIN MENU.")
        ch = int(input("\nENTER YOUR CHOICE:"))

        if ch == 1:
            print()
            fh_w = open("Past Tenant.txt", "a+")
            room = input("Enter room number:")
            name = input("Enter tenant name:")
            age = input("Enter age of tenant:")
            Phone_no = input("Enter Phone number:")
            email = input("Enter tenant email:")
            D_O_L = input("Enter date of leaving:")
            fh_w.write(room + "|" + name + "|" + age + "|" + Phone_no + "|" + email + "|" + D_O_L + "\n")
            fh_w.close()
            print("Record added!")
        if ch == 2:

            fh_r = open("Past Tenant.txt", "r")
            fh_w = open("temp.txt", "w")

            room = int(input("Enter room number to search:"))

            s = ' '
            while (s):
                s = fh_r.readline()
                L = s.split("|")
                if len(s) > 0:
                    if int(L[0]) == room:
                        room = input("Enter room number:")
                        name = input("Enter tenant name:")
                        age = input("Enter age of tenant:")
                        Phone_no = input("Enter Phone number:")
                        email = input("Enter tenant email:")
                        D_O_L = input("Enter date of leaving:")
                        fh_w.write(room + "|" + name + "|" + age + "|" + Phone_no + "|" + email + "|" + D_O_L + "\n")
                        fh_w.close()

            fh_w.close()
            fh_r.close()
            os.remove("Past Tenant.txt")
            os.rename("temp.txt", "Past Tenant.txt")

        if ch == 3:
            fh_r = open("Past Tenant.txt", "r")
            fh_w = open("temp.txt", "w")

            room = int(input("Enter room number to delete:"))

            s = ' '
            while (s):
                s = fh_r.readline()
                L = s.split("|")
                if len(s) > 0:
                    if int(L[0]) != room:
                        print("Delete successful!")
                        fh_w.write(s)

            fh_w.close()
            fh_r.close()
            os.remove("Past Tenant.txt")
            os.rename("temp.txt", "Past Tenant.txt")

        if ch == 4:
            return Main_menu()

#PAYMENT (SECOND OPTION UNDER Main_menu)

def PaymentForm():
    print("\n----------------------------------------------------------------\n"
          "\t                         PAYMENT MENU                              \n"
          "----------------------------------------------------------------  \n")

    option =[]
    while True:
        option = int(input("-----KINDLY PLEASE MAKE YOUR PAYMENT-----\n\n"
                                       "1. YES."
                                       "\t\t2. NO."
                                       "\n\nPLEASE SELECT A NUMBER TO CONFIRM YOUR PAYMENT:"))
        break
    if option == 1:
        Payment_detail()

    elif option == 2:
        return Main_menu()

def Payment_detail():
    print("\n\n*************  ONLINE BANKING METHODS  *************\n\n")

    payment_method = []
    while True:
        payment_method = int(input("1. MAYBANK\n"
                                   "2. PUBLIC BANK\n"
                                   "3. CIMB BANK\n"
                                   "4. CANCEL PAYMENT\n"
                                   "\nPLEASE SELECT WHICH BANKING METHOD TO PROCEED:"))
        break
    if payment_method == 1:
        MAYBANK()
    elif payment_method == 2:
        PBB()
    elif payment_method == 3:
        CIMB()
    elif payment_method == 4:
        return Main_menu()

def MAYBANK():
    while True:
        import datetime
        current_datetime1 = datetime.datetime.now()
        name = input("PLEASE ENTER YOU FULL NAME PER IC:")
        banking1 = input("PLEASE ENTER YOUR MAYBANK ACCOUNT NO:")
        if len(banking1) < 10:
            print("\n***** THERE'S A 8 DIGITS FOR YOUR ACC NUMBERS *****\n")
        elif len(banking1) > 11:
            print("\n***** YOUR ACCOUNT NUMBER IS TOO LONG *****\n")
        elif not any(char.isdigit() for char in banking1):
            print("\n***** YOUR ACCOUNT NUMBER IS INVALID *****\n")
        else:
            while True:
                confirm1 = input("PLEASE RE-CONFIRM YOUR ACOUNT NO:")
                if confirm1 == banking1:
                    print("\n***** YOUR ACCOUNT SUCCESSFULLY VERIFIED *****\n")
                    print(current_datetime1)

                    option = int(input("\n1. EXIT TO MAIN MENU."
                                       "\t\t2. RETURN TO PAYMENT DETAILS.\n\n"
                                       "PLEASE SELECT A NUMBER TO PROCEED:"))
                    if option == 1:
                        return Main_menu()
                    elif option == 2:
                        return Payment_detail()

                elif confirm1 != banking1:
                    print("\n***** PLEASE TRY IT AGAIN... THE PASSWORD IS NOT MATCH! *****\n")

def PBB():
    while True:
        import datetime
        current_datetime2 = datetime.datetime.now()
        name = input("PLEASE ENTER YOU FULL NAME PER IC:")
        banking2 = input("PLEASE ENTER YOUR PUBLIC BANK ACCOUNT NO:")
        if len(banking2) < 10:
            print("\n***** THERE'S A 8 DIGITS FOR YOUR ACC NUMBERS *****\n")
        elif len(banking2) > 11:
            print("\n***** YOUR ACCOUNT NUMBER IS TOO LONG *****\n")
        elif not any(char.isdigit() for char in banking2):
            print("\n***** YOUR ACCOUNT NUMBER IS INVALID *****\n")
        else:
            while True:
                confirm2 = input("PLEASE RE-CONFIRM YOUR ACOUNT NO:")
                if confirm2 == banking2:
                    print("\n***** YOUR ACCOUNT SUCCESSFULLY VERIFIED *****\n")
                    print(current_datetime2)

                    option = int(input("\n1. EXIT TO MAIN MENU."
                                       "\t\t2. RETURN TO PAYMENT DETAILS.\n\n"
                                       "PLEASE SELECT A NUMBER TO PROCEED:"))
                    if option == 1:
                        return Main_menu()
                    elif option == 2:
                        return Payment_detail()

                elif confirm2 != banking2:
                    print("\n***** PLEASE TRY IT AGAIN... THE PASSWORD IS NOT MATCH! *****\n")

def CIMB():
    while True:
        import datetime
        current_datetime3 = datetime.datetime.now()
        name = input("PLEASE ENTER YOU FULL NAME PER IC:")
        banking3 = input("PLEASE ENTER YOUR CIMB BANK ACCOUNT NO:")
        if len(banking3) < 10:
            print("\n***** THERE'S A 8 DIGITS FOR YOUR ACC NUMBERS *****\n")
        elif len(banking3) > 11:
            print("\n***** YOUR ACCOUNT NUMBER IS TOO LONG *****\n")
        elif not any(char.isdigit() for char in banking3):
            print("\n***** YOUR ACCOUNT NUMBER IS INVALID *****\n")
        else:
            while True:
                confirm3 = input("PLEASE RE-CONFIRM YOUR ACOUNT NO:")
                if confirm3 == banking3:
                    print("\n***** YOUR ACCOUNT SUCCESSFULLY VERIFIED *****\n")
                    print(current_datetime3)

                    option = int(input("\n1. EXIT TO MAIN MENU."
                                       "\t\t2. RETURN TO PAYMENT DETAILS.\n\n"
                                       "PLEASE SELECT A NUMBER TO PROCEED:"))
                    if option == 1:
                        return Main_menu()
                    elif option == 2:
                        return Payment_detail()

                elif confirm3 != banking3:
                    print("\n***** PLEASE TRY IT AGAIN... THE PASSWORD IS NOT MATCH! *****\n")

Main_menu()


