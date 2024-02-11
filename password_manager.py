print("Welcome to Prestons Password Solutions")
while True:
        
        
        print("\n")

        print("1.Register")
        print("2.Login")
        print("3.Exit")

        user_choice = input("Choose an option from above: ")

        if user_choice == '1':
            #register user
            print('print')
        elif user_choice == '2':
                #user login


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
                    print('block')

                elif user_choice2 == '2':
                    #search logins
                    print('block')

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
        
