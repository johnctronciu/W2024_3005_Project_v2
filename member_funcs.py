from config import load_config
from connect import connect

def userRegistration(first_name, last_name, email, start_date, weight, bodyfat_percent, card_no, cost): #Add student to database
    config = load_config()
    connection = connect(config)
    print("\nRegistering member...")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("insert into members (first_name, last_name, email, start_date, weight, bodyfat_percent, card_no, membership_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", (first_name, last_name, email, start_date, weight, bodyfat_percent, card_no, cost)) #SQL statement to insert
            connection.commit() #Commit any pending transaction to the database.
            connection.close()
    
    print("New member successfully added with data:", first_name, last_name, email, start_date, weight, bodyfat_percent, card_no)
    print("")

def addGoal(member_id, goal):
    config = load_config()
    connection = connect(config)
    print("\Adding goal...")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("insert into goals (member_id, goal) VALUES (%s, %s);", (member_id, goal)) #SQL statement to insert
            connection.commit() #Commit any pending transaction to the database.
            connection.close()
    
    print("New goal successfully added with data:", member_id, goal)
    print("")
    
def userDisplay(member_id):
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from members where member_id=%s", member_id) #Execute SQL statement
            row = cur.fetchone() #Get one rows/entries of data

            print("\nDisplaying member dashboard\n")
            print("Health Metrics and User information")
            print("-----------------------------------------")
            print(row)
            
            cur.execute("select * from goals where member_id=%s", member_id) #Execute SQL statement
            rows = cur.fetchall() #Get all rows/entries of data

            print("\nGoals")
            print("-----------------------------------------")
            for row in rows:
                print(row)

                #print(row[0]) Can get IDs like this and put them in an array to check before deletion? But then will we iterate through the array each time? Or make it a global variable?
                # Dont need to for this assignment, beyond scope I think
    print("")
    connection.close()

def schedulePersonal(member_id, trainer_id, session_date, session_start, session_end): # TODO:check times dont conflict
    config = load_config()
    connection = connect(config)
    print("\nBooking personal session...")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:


            cur.execute("insert into personalSession (member_id, trainer_id, session_date, session_start, session_end) VALUES (%s, %s, %s, %s, %s);", (member_id, trainer_id, session_date, session_start, session_end)) #SQL statement to insert
            connection.commit() #Commit any pending transaction to the database.
            connection.close()
    
    print("Personal session booked successfully with data:", member_id, trainer_id, session_date, session_start,session_end)
    print("")

def updateProfile(member_id,first_name=None,last_name=None,email=None,weight=None,bodyfat_percent=None,card_no=None, membership_cost=None):
    config = load_config()
    connection = connect(config)
    if (connection != None):
        with connection.cursor() as cur:
            fields = []
            values = []
            
            if first_name:
                fields.append("first_name = %s")
                values.append(first_name)
            if last_name:
                fields.append("last_name = %s")
                values.append(last_name)
            if email:
                fields.append("email = %s")
                values.append(email)
            if weight:
                fields.append("weight = %s")
                values.append(weight)
            if bodyfat_percent:
                fields.append("bodyfat_percent = %s")
                values.append(bodyfat_percent)
            if card_no:
                fields.append("card_no = %s")
                values.append(card_no)
            if membership_cost:
                fields.append("membership_cost = %s")
                values.append(membership_cost)
            values.append(member_id)
            print("update members set " + ", ".join(fields) + " where member_id = %s;", tuple(values))
            cur.execute("update members set " + ", ".join(fields) + " where member_id = %s;", tuple(values))
            connection.commit()
            connection.close()

def viewClasses():
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from groupClass") #Execute SQL statement
            rows = cur.fetchall() #Get all rows/entries of data

            print("\nDisplaying available classes")
            print("-----------------------------------------")
            for row in rows:
                print(row)

def bookClass(member_id, class_id):
    config = load_config()
    connection = connect(config)
    print("\nBooking personal session...")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("insert into classList (member_id, class_id) VALUES (%s, %s);", (member_id, class_id)) #SQL statement to insert
            connection.commit() #Commit any pending transaction to the database.
            connection.close()
    
    print("Personal session booked successfully with data:", member_id, class_id)
    print("")

if __name__ == '__main__':
    #updateProfile('1', weight='200')
    #userRegistration("Adam","Joe","adam.joe@example.com","2024-04-03", "250","30","716234875")
    #addGoal('1', "Reach 25% body fat")
    userDisplay('1')
    viewClasses()