import json, getpass, os, sys, pyfiglet, pyperclip
import socket, time
from cryptography.fernet import Fernet


def main():
    welcome = pyfiglet.figlet_format("Welcome to Preston's Password Solutions")
    print(welcome)

    print('\n')
    
    print('**************************************************************************')
    print('*                                WARNING!                                *')
    print('*                                                                        *')
    print('* This software is experimental and should NOT be considered secure. Do  *')
    print("* NOT use this software with ANY expectation that it's a secure OR       *")
    print('* private application for storing your passwords or other sensitive      *')
    print('* information.                                                           *')
    print('*                                                                        *')
    print('**************************************************************************')

    while True:    
        
        print("\n")

        print("1.Register")
        print("2.Login")
        print("3.More Information")
        print('4.Help')
        print("5.Exit")

        user_choice = input("Choose an option from above: ")

        if user_choice == '1':#register user
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


                    if user_choice2 == '1':#create login
                        website = input("Enter the website name: ")

                        username = input("Enter your username: ")

                        note = input("Enter a note (optional): ")

                        length = input('Enter the length of your desired password(max 50): ')

                        create_login(website, username, note, length)
                        print("Login added sucessfully")

                    elif user_choice2 == '2':
                        while True:#search logins
                            print("1.Search by website name")
                            print("2.Search by username")
                            print("3.Exit")

                            user_choice3 = input("Choose an option from above: ")

                            if user_choice3 == '1':
                                entered_website = input("Enter the name of the website you want to find login information for: ")
                            
                                find_login_by_website(entered_website)
                                break
                            elif user_choice3 == '2':
                                entered_username = input("Enter the username you want to search for log in information for: ")

                                find_login_by_username(entered_username)
                                break
                            elif user_choice3 == '3':
                                break


                    
                    elif user_choice2 == '3':
                        while True:#update login
                            print("1.Update website")
                            print("2.Update username")
                            print("3.Update note")
                            print('4.Update password')
                            print("5.Exit")

                            user_choice3 = input("Choose an option from above: ")

                            if user_choice3 == '1':
                                entered_website = input("Enter the name of the website for which you want to update login information for: ")
                                new_website = input("Enter the new website: ")

                                update_website(entered_website, new_website)

                            elif user_choice3 == '2': 
                                entered_website = input("Enter the name of the website for which you want to update login information for: ")
                                new_username = input("Enter your new username: ")

                                update_username(entered_website, new_username)

                            elif user_choice3 == '3':
                                entered_website = input("Enter the name of the website for which you want to update login information for: ")
                                new_note = input("Enter your new note: ")

                                update_note(entered_website, new_note)

                            elif user_choice3 == '4':
                                entered_website = input("Enter the name of the website for which you'd like to generate a new password for: ")
                                length = input('Enter the length of your desired password(max 50): ')
                                update_password(entered_website, length)

                            elif user_choice3 == '5':
                                break



                    elif user_choice2 == '4':
                        entered_website = input("Enter the name of the website whos login information you want to delete: ")
                        u_sure = f"Are you sure you want to delete {entered_website} ?"
                        print(u_sure)
                        to_delete = input("y/n: ")
                        if to_delete =='y':
                            delete_login(entered_website)
                        elif to_delete =='n':
                            print("Login delete aborted")
                            break

                    elif user_choice2 == '5':
                        break
        elif user_choice == '3':
            while(True):#show user more information
                print('\n')
                print('**************************************************************************')
                print('*                        More Information                                *')
                print('*                                                                        *')
                print("* - This software is a password manager that stores your passwords       *")
                print("*   locally on your machine in a json file. Your passwords are generated *")
                print('*   by a microservice, encrypted, sent back to your machine, decrypted,  *')
                print("*   and stored on your machine with your other login information.        *")
                print('*                                                                        *')
                print('* - Login information you can save include website name, username,       *')
                print('*   password, and an optional note.                                      *')
                print('*                                                                        *')
                print('* - Login functionality you can perform with this program is creating    *')
                print('*   an account, creating a login, updating a login, searching for        *')
                print('*   logins, and deleteing a login.                                       *')
                print('*                                                                        *')
                print('**************************************************************************')
                ex = input('Enter "e" to exit: ')
                if ex == 'e':
                    break



        elif user_choice == '4':
            while(True):#help menu
                print('**************************************************************************')
                print('*                               Help                                     *')
                print('*                                                                        *')
                print('* - To navigate this application, type the number corresponding to the   *')
                print('*   section of the program you want to navigate to, then press enter.    *')
                print('*                                                                        *')
                print('* - You can always return to the previous menu by typing the number      *')
                print('*   next to the "Exit" option. Or you will enter "e" to exit if there    *')
                print('*   is only one option.                                                  *')
                print('*                                                                        *')
                print('**************************************************************************')
                ex = input('Enter "e" to exit: ')
                if ex == 'e':
                    break

        elif user_choice == '5': #exit
            break


#function for registering user
def register(master_password):
    user_mp = {'master_password': master_password}
    file_name = 'user_mp.json'

    if os.path.exists(file_name) and os.path.getsize(file_name) ==0:
        with open(file_name, 'w') as file:
            json.dump(user_mp, file)
            print("Registration successfull! You can now log in\n")

    else:
        with open(file_name, 'x') as file:
            json.dump(user_mp, file)
            print("Registration successfull! You can now log in\n")



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



def create_login(website, username, note, length):
    if not os.path.exists('logins.json'): #if logins.json doesnt exit init it with empty list 
        login_arr = []

    else: 
        try:
            with open('logins.json', 'r') as file: #load logins from logins.json
                login_arr = json.load(file)

        except json.JSONDecodeError: #handle empty logins,json or invalid json 
            login_arr = []

    password = create_password(length)

    login_entry = {'website': website, 'username': username, 'note': note, 'password': password}
    login_arr.append(login_entry)
 
    with open('logins.json', 'w') as file: #save list
        json.dump(login_arr, file, indent = 4)



def find_login_by_website(entered_website): 
    if not os.path.exists('logins.json'): #check is logins.json exists
        return None

    try:
        with open('logins.json', 'r') as file:
            login_arr = json.load(file)

    except json.JSONDecodeError:
        login_arr = []
 
    found = False
    for entry in login_arr: #loop through logins to find login info mathcing website
        if entry['website'] == entered_website:
            found = True
            print("Website: ", entry['website'])
            print("Username: ", entry['username'])
            print("Note: ", entry['note'])
            print("Password: ", entry['password'])
    
    if found == False:
        print('Login not found')
   
    file.close()



def find_login_by_username(entered_username): 
    if not os.path.exists('logins.json'):  #check if logins.json exists
        return None

    try:
        with open('logins.json', 'r') as file:

            login_arr = json.load(file)

    except json.JSONDecodeError:
        login_arr = []
 
    for entry in login_arr: #loop through logins to find login info mathcing website
        if entry['username'] == entered_username:
            print("Website: ", entry['website'])
            print("Username: ", entry['username'])
            print("Note: ", entry['note'])
            print('Password: ', entry['password'])
        
    file.close()
 


def update_website(entered_website, new_website):
    with open('logins.json', 'r') as file:
        login_arr = json.load(file)
 
    for index, entry in enumerate(login_arr):  #use enumerate to get both index and entry
        if entry['website'] == entered_website:
            login_arr[index]['website'] = new_website

    with open('logins.json', 'w') as file:
        json.dump(login_arr, file)

    file.close()
    print("Website updated!")



def update_username(entered_website, new_username):
    with open('logins.json', 'r') as file:
        login_arr = json.load(file)

    for index, entry in enumerate(login_arr):
        if entry['website'] == entered_website:
            login_arr[index]['username'] = new_username

    with open('logins.json', 'w') as file:
        json.dump(login_arr, file)

    file.close()
    print("Username updated!")



def update_note(entered_website, new_note):
    with open('logins.json', 'r') as file:
        login_arr = json.load(file)

    for index, entry in enumerate(login_arr):
        if entry['website'] == entered_website:
            login_arr[index]['note'] = new_note

    with open('logins.json', 'w') as file:
        json.dump(login_arr, file)

    file.close()
    print("Note updated!")



def update_password(entered_website, length):

    new_password = create_password(length)

    with open('logins.json', 'r') as file:
        login_arr = json.load(file)

    for index, entry in enumerate(login_arr):
        if entry['website'] == entered_website:
            login_arr[index]['password'] = new_password

    with open('logins.json', 'w') as file:
        json.dump(login_arr, file)

    file.close()
    print("Password updated!")



def delete_login(entered_website):
    with open('logins.json', 'r') as file:
        login_arr = json.load(file)

    found = False
    for index, entry in enumerate(login_arr):  #use enumerate to get both index and entry
        if entry['website'] == entered_website:
            found = True
            login_arr[index]['website'] = 'NULL'
            login_arr[index]['username'] = 'NULL'
            login_arr[index]['note'] = 'NULL'
            login_arr[index]['password'] = 'NULL'


            with open('logins.json', 'w') as file:
                json.dump(login_arr, file)

    if found == False:
        print('login not found')
    else:
        print("Login deleted")

        file.close()
        


def decrypt_password(key, encrypted_password):
    cipher = Fernet(key)
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password



#calls microservice with int length, recieves ciphertext, decrypts, stores in json
def create_password(length):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#connect to server
    client_socket.connect(('localhost', 12345))

    client_socket.send(length.encode())#send length of password to be generated

    key = client_socket.recv(1024)#recieve key
    encrypted_password = client_socket.recv(1024)#recieve ciphertext

    decrypted_password = decrypt_password(key, encrypted_password)#decrypt password

    client_socket.close()

    return decrypted_password



if __name__ == '__main__':
    main()
