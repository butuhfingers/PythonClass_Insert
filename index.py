from Queries import Query
from Database import Database
import uuid

#Test Input
"""
firstName = "O'Brian"
lastName = "Crew"
address = "287 cutter lane"
city = "Billings"
state = "Montana"
postalCode = "59101-9384"
phoneNumber = "406-839-3947"
email = "fakeemail@derkalerk.ninja"
"""

#Take in input
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
address = input("Enter address: ")
city = input("Enter city: ")
state = input("Enter state: ")
postalCode = input("Enter postal code: ")
phoneNumber = input("Enter phone number: ")
email = input("Enter email: ")


#Start the database connection
database = Database()
query = Query()

#Get the proper UUIDs
mainUUID = uuid.uuid1()
phoneUUID = uuid.uuid4()
emailUUID = uuid.uuid4()

#Insert into the UUID table for names
database.Insert(query.Insert(database.connection,
                             "UUIDS",
                             "UUID, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT",
                             "'{}', 'Me-Derek', NOW()".format(mainUUID)))
#Insert into the UUID table for emails
database.Insert(query.Insert(database.connection,
                             "UUIDS",
                             "UUID, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT",
                             "'{}', 'Me-Derek', NOW()".format(emailUUID)))
#Insert into the UUID table for phone numbers
database.Insert(query.Insert(database.connection,
                             "UUIDS",
                             "UUID, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT",
                             "'{}', 'Me-Derek', NOW()".format(phoneUUID)))


#Insert into the NAMES table
database.Insert(query.Insert(database.connection,
                             "NAMES",
                             "UUID, FIRST_NM, LAST_NM, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT",
                             "'{0}', '{1}', '{2}', 'Me-Derek', NOW()".format(mainUUID,
                                                                             database.connection.escape_string(firstName),
                                                                             database.connection.escape_string(lastName))))

#Insert into the ADDRESSES table
database.Insert(query.Insert(database.connection,
                             "ADDRESSES",
                             "UUID, STREET, CITY, STATE_PROV, POSTAL_CODE, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT",
                             "'{0}', '{1}', '{2}', '{3}', '{4}', 'Me-Derek', NOW()".format(mainUUID,
                                                                                            database.connection.escape_string(address),
                                                                                            database.connection.escape_string(city),
                                                                                            database.connection.escape_string(state),
                                                                                            database.connection.escape_string(postalCode))))

#Insert into the EMAILS table
database.Insert(query.Insert(database.connection,
                             "EMAILS",
                             "UUID, OWNER_UUID, EMAIL_ADDRESS, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT",
                             "'{0}', '{1}', '{2}', 'Me-Derek', NOW()".format(emailUUID,
                                                                                              mainUUID,
                                                                                              database.connection.escape_string(email))))

#Insert into the PHONE NUMBERS table
database.Insert(query.Insert(database.connection,
                             "PHONE_DESC_VT",
                             "UUID, PHONE_DESC, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT",
                             "'{0}', 'Mobile', 'Me-Derek', NOW()".format(phoneUUID)))

#Insert into the PHONE NUMBERS_DESC table
database.Insert(query.Insert(database.connection,
                             "PHONE_NUMBERS",
                             "PHONE_DESC_UUID, OWNER_UUID, PHONE_NUMBER, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT",
                             "'{0}', '{1}', '{2}', 'Me-Derek', NOW()".format(phoneUUID,
                                                                                      mainUUID,
                                                                                      database.connection.escape_string(phoneNumber))))

database.Close()