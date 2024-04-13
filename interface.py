import member_funcs
import trainer_funcs
import admin_funcs

from datetime import date

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
            print("What action would you like to perform?")
            print("---------------------------------------------------------")
            print("1. View Profile \n2. Update information\n3. Schedule Management\n")
            print("Type 'quit' to quit the program\n")
            action = input("Action: ")
            if (action == '1'):
                member_id = input("Enter your memeber ID: ")
                member_funcs.userDisplay(member_id)
            elif (action == '2'):
                print("1. Add goal \n2. Update personal information\n")
                if (action== '1'):
                    member_id = input("Enter your member ID: ")
                    goal = input("Enter your goal: ")
                    member_funcs.addGoal(member_id, goal)
                elif (action == '2'):
                    print("Leave entry blank to not update...")
                    member_id = input("Enter your member ID: ")
                    first_name = input("Please enter your first name: ")
                    last_name = input("Please enter your last name: ")
                    email = input("Please enter your email: ")
                    weight = input("Please enter your weight: ")
                    bodyfat_percent = input("Please enter your body fat percentage: ")
                    card_no = input("Please enter your credit card number: ")
                    cost = input("Please enter your membership cost: ")
                    member_funcs.updateProfile(member_id, first_name,last_name,email,weight,bodyfat_percent,card_no,cost)
            elif (action == '3'):
                print("1. Schedule a private session \n2. Schedule a group class\n")
                if (action== '1'):
                    member_id = input("Enter your member ID: ")
                    trainer_id = input("Enter the trainer you would like to schedule with: ")
                    date = input("Enter desired date of session: ")
                    start_time = input("Enter desired start time: ")
                    end_time = input("Enter desired end time: ")
                    member_funcs.schedulePersonal(member_id, trainer_id, date, start_time, end_time)
                elif (action == '2'):
                    print("Available classes...")
                    member_funcs.viewClasses()
                    member_id = input("Enter your member ID: ")
                    class_id = input("Enter the class you would like to join: ")
                    member_funcs.bookClass(member_id, class_id)
        else:
            print("Would you like to join as a new member?")
            print("---------------------------------------------------------")
            print("1. Yes \n2. No\n")
            register = input("Action: ")
            if (register == '1'):
                first_name = input("Please enter your first name: ")
                last_name = input("Please enter your last name: ")
                email = input("Please enter your email: ")
                start_date = date.today()
                weight = input("Please enter your weight: ")
                bodyfat_percent = input("Please enter your body fat percentage: ")
                card_no = input("Please enter your credit card number: ")
                cost = input("Please enter your membership cost: ")
                member_funcs.userRegistration(first_name, last_name, email, start_date, weight, bodyfat_percent, card_no, cost)
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
            print("1. View booked rooms\n2. Book room\n3. Unbook room\n4. Update Room Booking\n")
            if (action =='1'):
                admin_funcs.checkBookedRooms()
            elif (action =='2'):
                room_no = input("Enter the room to be booked: ")
                class_id = input("Enter the class to be booked in the room: ")
                admin_funcs.bookRoom(room_no, class_id)
            elif (action =='3'):
                room_no = input("Enter the room to be unbooked: ")
                admin_funcs.unbookRoom(room_no)
            elif (action =='4'):
                class_id = input("Enter the class ID to be updated: ")
                room_no = input("Enter the new room for the class: ")
                admin_funcs.updateRoomBooking(room_no, class_id)
        elif (action == '2'):
            print("1. View All Equipment\n2. View equipment in need of maintenance\n3. Maintain equipment\n4. Add equipment\n5. Remove equipment\n")
            if (action =='1'):
                admin_funcs.getEquipmentList()
            elif (action =='2'):
                admin_funcs.inNeedofMaintenance()
            elif (action =='3'):
                equipment_id = input("Enter the equipment you maintained: ")
                admin_funcs.maintainEquipment(equipment_id)
            elif (action =='4'):
                equipment_name = input("Enter the name of the equipment to add: ")
                maintainence_days = input("Enter how many days per maintainence: ")
                admin_funcs.addEquipment(equipment_name, maintainence_days)
            elif (action == '5'):
                equipment_id = input("Enter the equipment to remove: ")
                admin_funcs.removeEquipment(equipment_id)

        elif (action == '3'):
            #TODO: IMPLEMENT MANAGE ROOM BOOKIGNS
            pass
        elif (action == '4'):
            member_id = input("Enter the member you want to see the billing of: ")
            admin_funcs.getBilling(member_id)
        elif (action == '5'):
            member_id = input("Enter the ID of the member to retrieve payment from: ")
            admin_funcs.retrievePayment(member_id)
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
            print("1. Add availability\n2. Delete availability\n3. Update availability\n")
            if(action == '1'):
                trainer_id = input("Enter your trainer ID: ") 
                available = input("Enter the date you are available: ")
                start = input("Enter your start time: ")
                end = input("Enter your end time: ")
                trainer_funcs.addAvailability(trainer_id, available,start,end)
            elif (action =='2'):
                trainer_id = input("Enter your trainer ID: ") 
                not_available = input("Enter the date you are no longer available: ")
                trainer_funcs.deleteAvailibility(trainer_id, not_available)
            elif (action =='3'):
                trainer_id = input("Enter your trainer ID: ") 
                available = input("Enter the date you are wish to edit: ")
                print("Leave blank to not update...")
                start = input("Enter your new start time: ")
                end = input("Enter your new end time: ")
                trainer_funcs.updateAvailibility(trainer_id,available,start,end)
        elif (action == '2'):
            member_first = input("Enter the first name of the number you would like to view: ")
            member_last = input("Enter the last name of the member you would like to view: ")
            trainer_funcs.searchMemberProfile(member_first, member_last)
            trainer_funcs.getMemberSession(member_first,member_last)
            trainer_funcs.getMemberClass(member_first,member_last)
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
