import pymysql

class Database:
#Information for the database

    def __init__(self):
        host = "scritch.ninja"
        database = "normalized"
        user = "derekadmin"
        password = "runner1994!"
        port = 3306
        connection = None;

        self.Connect()

    def Connect(self):
#Attempt the connection
        try:
            self.connection = pymysql.connect(host = "scritch.ninja",
                                        port = 3306,
                                        user = "derekadmin",
                                        password = "runner1994!",
                                        database = "normalized")
            print("Connected to the database")
# Something went wrong connecting to the database
        except:
            print("Ooops... we goofed somewhere!")

        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)

#Insert into the database
    def Insert(self, query):
        print("ATTEMPTING: {}".format(query))

        self.cursor.execute(query)
        self.connection.commit()

        print("EXECUTED: {}\n".format(query))

    def Close(self):
        self.cursor.close()
        self.connection.close()