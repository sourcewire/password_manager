import json, getpass, os, sys


def password_manager():
    print("Welcome to Prestons Password Solutions")
    while True:    
        
        print("\n")

        print("1.Register")
        print("2.Login")
        print("3.Exit")

        user_choice = input("Choose an option from above: ")

        if user_choice == '1':
            #register user
            file = 'user_mp.json'

            if os.path.exists(file) and os.path.getsize(file) != 0:
                print("\n You've already created a master password")
                sys.exit()

            else:
                master_password = getpass.getpass("Enter a master password of your choice: ")
                register(master_password)

        elif user_choice == '2': # user logs in
                file = 'user_mp.json'

                if os.path.exists(file):
                    master_password = getpass.getpass("Enter your master password: ")
                    login(master_password)

                else:
                    print("You need to register before logging in")
                    sys.exit()


                while True: 
                    print("\n")
                    print("1.Create Login")
                    print("2.Search Logins")
                    print("3.Update Login")
                    print("4.Delete Login")
                    print("5.Exit")

                    user_choice2 = input("Choose an option from above: ")
                    print("\n")
                    if user_choice2 == '1':
                        #create login
                        website = input("Enter the website name: ")

                        username = input("Enter your username: ")

                        note = input("Enter a note (optional): ")

                        create_login(website, username, note)
                        print("Login added sucessfully")

                    elif user_choice2 == '2':
                        #search logins
                        print("1.Search by website name")
                        print("2.Search by username")
                        print("3.Exit")

                        user_choice3 = input("Choose an option from above: ")

                        if user_choice3 == '1':
                            entered_website = input("Enter the name of the website you want to find login information for: ")
                            
                            find_login_by_website(entered_website)

                        elif user_choice == '2':
                            entered_username = input("Enter the username you want to search for log in information for: ")

                            find_login_by_username(entered_username)

                        elif user_choice == '3':
                            sys.exit()



                    elif user_choice2 == '3':
                        #update login
                        print('block')

                    elif user_choice2 == '4':
                        #delete login
                        print('block')

                    elif user_choice2 == '5':
                        break

        elif user_choice == '3':
            #exit
            break


#function for registering user
def register(master_password):
    user_mp = {'master_password': master_password}
    file_name = 'user_mp.json'

    if os.path.exists(file_name) and os.path.getsize(file_name) ==0:
        with open(file_name, 'w') as file:
            json.dump(user_mp, file)
            print("Registration successfule! You can now log in\n")

    else:
        with open(file_name, 'x') as file:
            json.dump(user_mp, file)
            print("Registration successfule! You can now log in\n")



#function for logging in registered user
def login(entered_password):
    try:
        with open('user_mp.json', 'r') as file:
            user_mp = json.load(file)

        stored_password = user_mp.get('master_password')
        
        if entered_password == stored_password:
            print("You're logged in")

        else:
            print("Invalid password")

    except Exception:
        print("Please register before trying to log in")
        sys.exit()



#create new login -- not adding password functionality yet because it requires microservice
def create_login(website, username, note):
    if not os.path.exists('logins.json'):
        #if logins.json doesnt exit init it with empty list
        logins = []

    else:
        #load logins from logins.json
        try:
            with open('logins.json', 'r') as file:
                logins = json.load(file)

        except json.JSONDecodeError:
            #handle empty logins,json or invalid json
            logins = []


    login_entry = {'website': website, 'username': username, 'note': note}
    logins.append(login_entry)

    #save list
    with open('logins.json', 'w') as file:
        json.dump(logins, file, indent = 4)



#def find_login_by_website():



#def find_login_by_username():




if __name__ == '__main__':
    password_manager()
