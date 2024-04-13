from config import load_config
from connect import connect

def getAllStudents(): #Function to print all students
    config = load_config() #load config to get user data to connect to database
    connection = connect(config) #Connect
 
    if (connection != None):
        with connection.cursor() as cur:
            cur.execute("select student_id, first_name, last_name, email, enrollment_date from Students") #Execute SQL statement
            rows = cur.fetchall() #Get all rows/entries of data

            print("\nListing all Students")
            print("-----------------------------------------")
            for row in rows:
                print(row)
                #print(row[0]) Can get IDs like this and put them in an array to check before deletion? But then will we iterate through the array each time? Or make it a global variable?
                # Dont need to for this assignment, beyond scope I think
    print("")
    connection.close()