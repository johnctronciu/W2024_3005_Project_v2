#import DML

def mainPage():
    print("What is your role in the system?")
    print("---------------------------------------------------------")
    print("1. Member\n2. Administrator\n3. Trainer\n")
    print("Type 'quit' to quit the program\n")
    action = input("Action: ")

    return action

def memberInterface():
    print("Are you an existing member?")
    print("---------------------------------------------------------")
    print("1. Yes \n2. No\n")
    print("Type 'quit' to quit the program\n")
    action = input("Action: ")

    while (action != 'quit'):
        if (action == '1'):
            pass
        else:
            print("Would you like to join as a new member?")
            print("---------------------------------------------------------")
            print("1. Yes \n2. No\n")
            register = input("Action: ")
            if (register == '1'):
                # TODO: IMPLEMENT MEMBER REGISTRATION
                pass
            elif (register == '2'):
                print("Returning to main page...")
            elif (action.lower() != 'quit'):
                print("Returning to main page...")
            else:
                print("Invalid input!")

        print("Are you an existing member?")
        print("---------------------------------------------------------")
        print("1. Yes \n2. No\n")
        print("Type 'quit' to quit the program\n")
        action = input("Action: ")

def adminInterface():
    print("Welcome administrator...")
    print("---------------------------------------------------------")
    print("1. Manage room bookings\n2. Monitor fitness equipment maintenance\n"+
          "3. Update class schedule\n4. Oversee billing\n5. Process payments for membership fees, personal training sessions, and other services.")
    print("Type 'quit' to quit the program\n")
    action = input("Action: ")
    while (action.lower() != 'quit'):
        if (action == '1'):
            #TODO: IMPLEMENT MANAGE ROOM BOOKIGNS
            pass
        elif (action == '2'):
            #TODO: IMPLEMENT MANAGE ROOM BOOKIGNS
            pass
        elif (action == '3'):
            #TODO: IMPLEMENT MANAGE ROOM BOOKIGNS
            pass
        elif (action == '4'):
            #TODO: IMPLEMENT MANAGE ROOM BOOKIGNS
            pass
        elif (action == '5'):
            #TODO: IMPLEMENT MANAGE ROOM BOOKIGNS
            pass
        elif (action.lower() != 'quit'):
            print("Returning to main page...")
        else:
            print("Invalid input!")
        
        print("Welcome administrator...")
        print("---------------------------------------------------------")
        print("1. Manage room bookings\n2. Monitor fitness equipment maintenance\n"+
          "3. Update class schedule\n4. Oversee billing\n5. Process payments for membership fees, personal training sessions, and other services.")
        print("Type 'quit' to quit the program\n")
        action = input("Action: ")

def trainerInterface():
    print("Welcome trainer...")
    print("---------------------------------------------------------")
    print("1. Manage schedule\n2. View members\n")
    print("Type 'quit' to quit the program\n")
    action = input("Action: ")
    while (action.lower() != 'quit'):
        if (action == '1'):
            #TODO: IMPLEMENT MANAGE ROOM BOOKIGNS
            pass
        elif (action == '2'):
            #TODO: IMPLEMENT MANAGE ROOM BOOKIGNS
            pass
        elif (action.lower() != 'quit'):
            print("Returning to main page...")
        else:
            print("Invalid input!")
        
        print("Welcome trainer...")
        print("---------------------------------------------------------")
        print("1. Manage schedule\n2. View members\n")
        print("Type 'quit' to quit the program\n")
        action = input("Action: ")

def actionLoop():
    action = mainPage()

    while (action.lower() != 'quit'):
        if (action == '1'):
            memberInterface()

        
        elif (action == '2'):
            adminInterface()

        elif (action == '3'):
            trainerInterface()
        else:
            print("Invalid action, please try again")
        
        action = mainPage()
    
    print("Shutting down...")



if __name__ == '__main__':
    actionLoop()
