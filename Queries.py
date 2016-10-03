class Query:
    def Insert(self, connection, table, columns, values):
#Escape the strings givenS
        return "INSERT INTO {} ({}) VALUES({}) ".format(table, columns, values)
