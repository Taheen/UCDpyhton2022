# i'm creating restaurant booking system.
# you can check all the tables for availability.
# you can clear the reservation2, or you can overwrite existing booking.
# further extension can be added by adding an external list to facilitate
# more days/weeks(eventually - a calendar, but you will need a database for that)

class Restaurant:

    def __init__(self, amount_of_tables):
        self.amount_of_tables = amount_of_tables
        self.blank_table = [0, '-empty-', 123456789]
        self.tables = [self.blank_table for i in range(self.amount_of_tables)]

    def table_printout(self, input_table_number):
        n = input_table_number
        print("Table n." + str(n + 1))
        if self.tables[n][0] == 0:
            print(" - is available")
        else:
            print(" - time: " + str(self.tables[n][0]))
            print(" - name: " + self.tables[n][1])
            print(" - phone: " + str(self.tables[n][2]))

    # showing all tables
    def show_tables(self):
        for i in range(self.amount_of_tables):
            self.table_printout(i)

    # making a booking
    def book_table(self, number, time, name, phone):
        self.tables[number - 1] = [time, name, phone]

    # clearing a booking(setting a blank_table)
    def clear_table(self, number):
        self.tables[number - 1] = self.blank_table

    def int_input(user_int_input):
        while True:
            try:
                some_integer = int(input(user_int_input))
                return some_integer
            except ValueError as e:
                print("Not a proper number! Try again")


# creating a restaurant with 6 tables
rest1 = Restaurant(6)

# creating bookings for tables 1,3,4
rest1.book_table(1, 15, 'Smith', 863967861)
rest1.book_table(3, 18, 'Smith2', 864447861)
rest1.book_table(4, 17, 'Jones', 86000861)

exit1 = False

while not exit1:
    print("Please select an option:")
    print("1 - view tables, 2 - add booking, 3 - clear booking, 0 - EXIT")

#checking for proper input type
    while True:
        try:
            userinput = int(input())
            break
        except ValueError:
            print("Not a valid number.  Try again...")

    if userinput == 1:
        print(rest1.show_tables())

    if userinput == 2:
        print("Select table number:")
        user_input_table_number = int(input())
        if rest1.tables[user_input_table_number - 1][0] != 0:
            print("Table n. " + str(user_input_table_number) + " is booked")
        else:
            print("Choose time (between 2pm and 9pm):")
            while True:
                try:
                    table_time = int(input())
                    break
                except ValueError:
                    print("Not a valid number.  Try again...")

            if table_time < 2 or table_time > 9:
                raise Exception('Time must be between 2 and 9. Selected time was: {}'.format(table_time))

            table_name = input("Enter name:")
            table_phone = input("Enter phone number:")
            rest1.book_table(user_input_table_number, table_time, table_name, table_phone)

    if userinput == 3:
        print("Select table number:")
        user_input_table_number = int(input())
        rest1.clear_table(user_input_table_number)

    if userinput == 0:
        exit1 = True


