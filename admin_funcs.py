from config import load_config
from connect import connect

from datetime import datetime

def getTrainerTimes(trainer_id):
    avail = []
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect

 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from trainerSchedule where trainer_id=%s", trainer_id) #Execute SQL statement
            rows = cur.fetchall() #Get rows/entries of data
            for row in rows:
                avail.append((row[1],row[2],row[3]))
    connection.close()
    return avail


def checkTimes(date, start, end, avail):
    for slot in avail:
        date = datetime.strptime(str(date), '%Y-%m-%d').date()
        start = datetime.strptime(str(start), '%H:%M:%S').time()
        end = datetime.strptime(str(end), '%H:%M:%S').time()

        start_dt = datetime.combine(date,start)
        end_dt = datetime.combine(date,end)

        combined_start = datetime.combine(slot[0], slot[1])
        combined_end = datetime.combine(slot[0], slot[2])

        if (date == slot[0]):
            return start_dt >= combined_start and end_dt <= combined_end

def getEquipmentList():
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from equipment") #Execute SQL statement
            rows = cur.fetchall() #Get one rows/entries of data

            print("\nDisplaying equipment list")
            print("-----------------------------------------")
            for row in rows:
                print(row)

def inNeedofMaintenance():
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from equipment") #Execute SQL statement
            rows = cur.fetchall() #Get one rows/entries of data

            print("\nDisplaying equipment in need of maintenance")
            print("-----------------------------------------")
            for row in rows:
                if (row[4]== True):
                    print(row[0],row[1])

def maintainEquipment(equipment_id):
    config = load_config()
    connection = connect(config)
    print("\Maintaining equipment:")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("update equipment set last_maintenance_date=%s, needs_maintenance=%s where equipment_id=%s;", (datetime.today(),False, equipment_id)) #SQL Statement to update
            connection.commit() #Commit any pending transaction to the database.

            print("equipment successfully maintained\n")

            connection.close()

def addEquipment(equipment, days_per_maintenance):
    config = load_config()
    connection = connect(config)
    print("\Adding equipment...")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("insert into equipment (equipment, last_maintenance_date, days_per_maintenance, needs_maintenance) VALUES (%s, %s, %s, %s);", (equipment, datetime.today(), days_per_maintenance, False)) #SQL statement to insert
            connection.commit() #Commit any pending transaction to the database.
            connection.close()
    
    print("New equipment successfully added with data:", equipment, datetime.today(), days_per_maintenance, False)
    print("")

def removeEquipment(equipment_id):
    config = load_config()
    connection = connect(config)
    print("Removing equipment data:")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("delete from equipment where equipment_id=%s;", (equipment_id)) #SQL statement to delete
            connection.commit() #Commit any pending transaction to the database.

            print("Delete equipment Operation Successfully Recieved by Database\n")

            connection.close()

def checkBookedRooms():
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from classRoom") #Execute SQL statement
            rows = cur.fetchall() #Get one rows/entries of data

            print("\nDisplaying booked rooms")
            print("-----------------------------------------")
            for row in rows:
                print(row)

def bookRoom(room_no, class_id):
    config = load_config()
    connection = connect(config)
    print("\Adding booking...")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("insert into classRoom (room_no, class_id) VALUES (%s, %s);", (room_no, class_id)) #SQL statement to insert
            connection.commit() #Commit any pending transaction to the database.
            connection.close()
    
    print("New room successfully booked with data:", room_no, class_id)
    print("")

def unbookRoom(class_id):
    config = load_config()
    connection = connect(config)
    print("\Removing room booking data:")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("delete from classRoom where class_id=%s;", (class_id)) #SQL statement to delete
            connection.commit() #Commit any pending transaction to the database.

            print("Delete room booking Operation Successfully Recieved by Database\n")

            connection.close()
        
def updateRoomBooking(room_no, class_id):
    config = load_config()
    connection = connect(config)
    print("\Changing booking:")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("update classRoom set room_no=%s where class_id=%s;", (room_no, class_id)) #SQL Statement to update
            connection.commit() #Commit any pending transaction to the database.

            print("Room number successfully changed\n")

            connection.close()

def addGroupClass(class_date, class_start, class_end):
    config = load_config()
    connection = connect(config)
    print("\Adding class...")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("insert into groupClass (class_date, class_start, class_end) VALUES (%s, %s, %s);", (class_date, class_start, class_end)) #SQL statement to insert
            connection.commit() #Commit any pending transaction to the database.
            connection.close()
    
    print("New class successfully added with data:", class_date, class_start, class_end)
    print("")

def removeGroupClass(class_id):
    config = load_config()
    connection = connect(config)
    print("\Removing class data:")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("delete from groupClass where class_id=%s;", (class_id)) #SQL statement to delete
            connection.commit() #Commit any pending transaction to the database.

            print("Delete room booking Operation Successfully Recieved by Database\n")

            connection.close()
        
def updateGroupClass(class_id, class_date, class_start, class_end):
    config = load_config()
    connection = connect(config)
    if (connection != None):
        with connection.cursor() as cur:
            fields = []
            values = []
            
            if class_date:
                fields.append("class_date = %s")
                values.append(class_date)
            if class_start:
                fields.append("class_start = %s")
                values.append(class_start)
            if class_end:
                fields.append("class_end = %s")
                values.append(class_end)
            values.append(class_id)
            cur.execute("update groupClass set " + ", ".join(fields) + " where class_id = %s;", tuple(values))
            connection.commit()
            connection.close()

def assignTrainertoClass(trainer_id, class_id): #TODO: Check availability
    config = load_config()
    connection = connect(config)
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from groupClass where class_id=%s", class_id) #Execute SQL statement
            row = cur.fetchone() #Get rows/entries of data
            if not (checkTimes(row[0],row[1],row[2],getTrainerTimes(trainer_id))):
                print("Not a valid time...")
                return None 
            
            print("Assigning trainer...")
            print("-----------------------------------------")
            cur.execute("insert into assignedClass (trainer_id, class_id) VALUES (%s, %s);", (trainer_id, class_id)) #SQL statement to insert
            connection.commit() #Commit any pending transaction to the database.
            connection.close()
    
    print("New class successfully added with data:", trainer_id, class_id)
    print("")

def removeTrainerfromClass(trainer_id, class_id):
    config = load_config()
    connection = connect(config)
    print("\Removing trainer from class data:")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("delete from assignedClass where trainer_id=%s and class_id=%s;", (trainer_id, class_id)) #SQL statement to delete
            connection.commit() #Commit any pending transaction to the database.

            print("Delete trainer from class Operation Successfully Recieved by Database\n")

            connection.close()

#Payment stuff

def getBilling(member_id):
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from billing where member_id=%s", member_id) #Execute SQL statement
            rows = cur.fetchall() #Get one rows/entries of data

            print("\nDisplaying member billing information")
            print("-----------------------------------------")
            for row in rows:
                print(row)

    connection.close()

def retrievePayment(member_id):
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select * from members where member_id=%s", member_id) #Execute SQL statement
            row = cur.fetchone() #Get one rows/entries of data

            print("Proccessing payment for member %s, %s ID: %s, email: %s" % (row[1], row[2], member_id, row[3]))
            cur.execute("insert into billing (member_id, cost, card_no, transaction_date) VALUES (%s, %s, %s, %s);", (member_id, row[8], row[7], datetime.today())) #SQL statement to insert
            connection.commit()
            print("Amount Paid: $%s, Card Number: #%s" % (row[8], row[7]))

                #print(row[0]) Can get IDs like this and put them in an array to check before deletion? But then will we iterate through the array each time? Or make it a global variable?
                # Dont need to for this assignment, beyond scope I think
    print("")
    connection.close()



if __name__ == '__main__':
    #getEquipmentList()
    #inNeedofMaintenance()
    #maintainEquipment(2)
    retrievePayment("1")
