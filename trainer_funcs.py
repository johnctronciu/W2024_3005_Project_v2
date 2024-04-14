from config import load_config
from connect import connect

def addAvailability(trainer_id, available, start_time, end_time):
    config = load_config()
    connection = connect(config)
    print("Adding availability...")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("insert into trainerSchedule (trainer_id, available, start_time, end_time) VALUES (%s, %s, %s,%s);", (trainer_id, available, start_time, end_time)) #SQL statement to insert
            connection.commit() #Commit any pending transaction to the database.
            connection.close()
    
    print("New availibility successfully added with data:", trainer_id, available, start_time, end_time)
    print("")

def deleteAvailibility(trainer_id, available): #DELETE student data row from table
    config = load_config()
    connection = connect(config)
    print("\nDeleting availability data:")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("delete from trainerSchedule where trainer_id=%s and available=%s;", (trainer_id, available)) #SQL statement to delete
            connection.commit() #Commit any pending transaction to the database.

            print("Delete availability Operation Successfully Recieved by Database\n")

            connection.close()

def updateAvailibility(trainer_id, available,start_time=None,end_time=None):
    config = load_config()
    connection = connect(config)
    if (connection != None):
        with connection.cursor() as cur:
            fields = []
            values = []
            
            if start_time:
                fields.append("start_time = %s")
                values.append(start_time)
            if end_time:
                fields.append("end_time = %s")
                values.append(end_time)
            
            values.append(trainer_id)
            values.append(available)
            cur.execute("update trainerSchedule set " + ", ".join(fields) + " where trainer_id = %s and available = %s;", tuple(values))
            connection.commit()
            connection.close()

def getMemberSession(member_id):
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from personalSession where member_id=%s", (member_id)) #Execute SQL statement
            rows = cur.fetchall() #Get one rows/entries of data

            print("\nDisplaying member personal sessions")
            print("-----------------------------------------")
            for row in rows:
                print(row)

def getMemberClass(member_id):
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from classList where member_id=%s", (member_id)) #Execute SQL statement
            rows = cur.fetchall() #Get one rows/entries of data

            print("\nDisplaying member group classess")
            print("-----------------------------------------")
            for row in rows:
                print(row)

def searchMemberProfile(first_name, last_name):
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select member_id, first_name, last_name, email, start_date, weight, bodyfat_percent from members where first_name=%s and last_name=%s;", (first_name, last_name)) #Execute SQL statement
            rows = cur.fetchall() #Get one rows/entries of data
            
            print("\nDisplaying member dashboard\n")
            print("Health Metrics and User information")
            print("-----------------------------------------")
            for row in rows:
                member_id = row[0]
                print(row)
                getMemberSession(str(member_id))
                getMemberClass(str(member_id))