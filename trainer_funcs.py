from config import load_config
from connect import connect

def addAvailability(trainer_id, available, start_time, end_time):
    config = load_config()
    connection = connect(config)
    print("\Adding availability...")
    print("-----------------------------------------")
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("insert into trainerSchedule (trainer_id, available, start_time, end_time)) VALUES (%s, %s, %s,%s);", (trainer_id, available, start_time, end_time)) #SQL statement to insert
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

def updateAvailibility(trainer_id, available=None,start_time=None,end_time=None):
    config = load_config()
    connection = connect(config)
    if (connection != None):
        with connection.cursor() as cur:
            fields = []
            values = []
            
            if available:
                fields.append("available = %s")
                values.append(available)
            if start_time:
                fields.append("start_time = %s")
                values.append(start_time)
            if end_time:
                fields.append("end_time = %s")
                values.append(end_time)
            
            values.append(trainer_id)
            print("update trainerSchedule set " + ", ".join(fields) + " where trainer_id = %s;", tuple(values))
            cur.execute("update trainerSchedule set " + ", ".join(fields) + " where trainer_id = %s;", tuple(values))
            connection.commit()
            connection.close()

def